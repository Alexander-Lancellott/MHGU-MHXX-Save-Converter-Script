from art import tprint
from modules.utils import custom_logger, get_file, end, path, absolute_path, custom_input, clear

init_logger = custom_logger(__name__)
logger = init_logger["logger"]
yellow = init_logger["yellow"]
reset = init_logger["reset"]


def clear_screen():
    clear()
    tprint("MHXX TO MHGU-XX\n\n", font="tarty1")


def fix_chat(new_save_data, _3ds_file, slot_position, chat_position):
    chat_range = 100
    extra_chat_bytes = bytes(44)

    new_save_data += _3ds_file[slot_position:chat_position]
    for i in range(1, chat_range):
        new_save_data += (
            _3ds_file[chat_position + (60 * (i - 1)) : chat_position + (60 * i)]
            + extra_chat_bytes
        )

    return new_save_data


def mhxx_to_mhguxx():
    tprint("MHXX TO MHGU-XX\n\n", font="tarty1")

    file_path = "MHXX_TO_MHGU-XX - (3DS To Switch)/system"
    output_path = "MHXX_TO_MHGU-XX - (3DS To Switch)/output - (Switch)/system"

    mhgu_initial_position = 1625244
    mhxx_initial_position = 1205400
    slot_positions = [1205364, 2378801, 3552241]
    chat_positions = [2372861, 3546301, 4719741]
    chat_length = 5940

    _3ds_file = get_file(file_path, logger)

    if not _3ds_file:
        return

    if len(_3ds_file) != 4726152:
        logger.error("Invalid Format!! - Please use 3DS save data")
        return end()

    msg = (
        "Which game would you like to convert your save file to?\n\n"
        f"[{yellow}1{reset}] - MHGU\n"
        f"[{yellow}2{reset}] - MHXX Switch Version\n"
    )

    option = custom_input(msg, "Enter the number of the option: ", 2, logger, clear_screen)

    new_save_data = None

    if option == 1:
        blank_path = "Blank_Switch_Save/MHGU/system"
        blank = get_file(blank_path, logger)

        if not blank:
            return

        if len(blank) != 5159100:
            logger.error('Corrupt or wrong file in: %s"%s"%s', yellow, path(blank_path), reset)
            return end()

        new_save_data = blank[:40] + _3ds_file[4:8] + blank[44:mhgu_initial_position]

        # fix chat
        for i, chat_position in enumerate(chat_positions):
            new_save_data = fix_chat(
                new_save_data, _3ds_file, slot_positions[i], chat_position
            )

        new_save_data += _3ds_file[chat_positions[2] + chat_length :]
    else:
        blank_path = "Blank_Switch_Save/MHXX Switch Version/system"
        blank = get_file(blank_path, logger)

        if not blank:
            return

        if len(blank) != 4726188:
            logger.error('Corrupt or wrong file in: %s"%s"%s', yellow, path(blank_path), reset)
            return end()

        new_save_data = (
            blank[:40] + _3ds_file[4:8] +
            blank[44:mhxx_initial_position] +
            _3ds_file[slot_positions[0]:]
        )

    output = open(absolute_path(output_path), "wb")
    output.write(new_save_data)
    output.close()

    logger.info('File generated in: %s"%s"%s', yellow, path(output_path), reset)
    end()


if __name__ == "__main__":
    mhxx_to_mhguxx()
