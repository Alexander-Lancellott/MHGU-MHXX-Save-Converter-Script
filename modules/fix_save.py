from art import tprint
from modules.utils import (
    custom_logger,
    end,
    path,
    clear,
    get_file,
    custom_input,
)


init_logger = custom_logger(__name__)
logger = init_logger["logger"]
yellow = init_logger["yellow"]
reset = init_logger["reset"]


def clear_screen():
    clear()
    tprint("FIX SAVE\n\n", font="tarty1")


def fix_chat(
    new_save_data,
    switch_file,
    chat_position,
    current_slot_position,
    slot_position,
    is_position_slot_wrong,
    slot_wrong_position,
    option,
):
    chat_path = "FIX_SAVE - (Switch To Switch)/bin/chat"
    chat_length = 10296
    chat_range = 100
    extra_chat_bytes = bytes(44)
    position_difference = (
        slot_position - slot_wrong_position if is_position_slot_wrong else 0
    )
    new_save_data += switch_file[
        current_slot_position : (chat_position - position_difference)
    ]

    if option == 1:
        for i in range(1, chat_range):
            new_save_data += (
                switch_file[
                    (chat_position - position_difference)
                    + (60 * (i - 1)) : (chat_position - position_difference)
                    + (60 * i)
                ]
                + extra_chat_bytes
            )

        return new_save_data
    else:
        chat = get_file(chat_path, logger)

        if not chat:
            return

        if len(chat) != chat_length:
            logger.error(
                'Corrupt or wrong file in: %s"%s"%s', yellow, path(chat_path), reset
            )
            return end()

        return new_save_data + chat


def fix_save():
    tprint("FIX SAVE\n\n", font="tarty1")

    file_path = "FIX_SAVE - (Switch To Switch)/system"
    output_path = "FIX_SAVE - (Switch To Switch)/output - (Switch)/system"
    blank_path = "Blank_Switch_Save/MHGU/system"

    slot_positions = [1625244, 2803037, 3980833]
    slot_wrong_positions = [1205400, 2378837, 3552277]
    chat_positions = [2792741, 3970537, 5148333]
    chat_length = 10296

    switch_file = get_file(file_path, logger)

    if not switch_file:
        return

    if len(switch_file) != 5159100:
        logger.error("Invalid Format!! - Please use Switch save data")
        return end()

    slot1_validation = switch_file[
        slot_wrong_positions[0] : slot_wrong_positions[0] + 10
    ] != bytes(10)
    slot2_validation = False
    slot3_validation = False
    prev_slot_bytes = bytes(b"\xff\x8b\xa1P\xff")

    if switch_file[2525141 - 11 : 2525141 - 6] == prev_slot_bytes:
        slot2_validation = switch_file[2525141 : 2525141 + 10] != bytes(10)

    if switch_file[3698581 - 11 : 3698581 - 6] == prev_slot_bytes:
        slot3_validation = switch_file[3698581 : 3698581 + 10] != bytes(10)

    blank = get_file(blank_path, logger)

    if not blank:
        return

    if len(blank) != 5159100:
        logger.error(
            'Corrupt or wrong file in: %s"%s"%s', yellow, path(blank_path), reset
        )
        return end()

    is_position_slot_wrong = slot1_validation or slot2_validation or slot3_validation

    check_slot_positions = list(
        map(
            lambda position, wrong_position: (
                wrong_position if is_position_slot_wrong else position
            ),
            slot_positions,
            slot_wrong_positions,
        )
    )

    new_save_data = (
        blank[:40] + switch_file[40 : 43 + 1] + blank[44 : slot_positions[0]]
    )

    msg = (
        "What do you want to do with the chat menu?\n\n"
        f"[{yellow}1{reset}] - Try to recover it - (Mostly recommended if you didn't edit the chats in MHGU)\n"
        f"[{yellow}2{reset}] - Replace it with the English version of MHGU\n"
    )

    option = custom_input(
        msg, "Enter the number of the option: ", 2, logger, clear_screen
    )

    # fix chats
    for i, chat_position in enumerate(chat_positions):
        new_save_data = fix_chat(
            new_save_data,
            switch_file,
            chat_position,
            check_slot_positions[i],
            slot_positions[i],
            is_position_slot_wrong,
            slot_wrong_positions[i],
            option,
        )
        if not new_save_data:
            return

    new_save_data += switch_file[chat_positions[2] + chat_length :]

    output = open(output_path, "wb")
    output.write(new_save_data)
    output.close()

    logger.info('File generated in: %s"%s"%s', yellow, path(output_path), reset)
    end()


if __name__ == "__main__":
    fix_save()
