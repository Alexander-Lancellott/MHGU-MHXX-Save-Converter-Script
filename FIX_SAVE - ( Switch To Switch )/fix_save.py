from modules.utils import custom_logger, end, path
from art import *


init_logger = custom_logger(__name__)
logger = init_logger['logger']
yellow = init_logger['yellow']
reset = init_logger['reset']


def fix_chat(new_save_data, switch_file, start_position, end_position):
    chat_path = 'bin/chat'
    chat_length = 10296

    try:
        chat_file = open(chat_path, 'rb')
    except OSError:
        logger.error(f'No such a file or directory: {yellow}"{chat_path}"{reset}')
        end()
    with chat_file:
        chat = chat_file.read()
        chat_file.close()

    if len(chat) != chat_length:
        logger.error(f'Corrupt or wrong file in: {yellow}"{path(chat_path)}"{reset}')
        end()

    return new_save_data[:start_position] + chat + switch_file[end_position:]


def fix_save():
    file_path = 'system'
    output_path = 'output - (Switch)/system'
    blank_path = '../Blank_Switch_Save/system'

    slot1_position = 1625244
    slot2_position = 2803037
    slot3_position = 3980833
    slot1_wrong_position = 1205400
    slot2_wrong_position = 2378837
    slot3_wrong_position = 3552277
    chat1_position = 2792741
    chat2_position = 3970537
    chat3_position = 5148333
    chat_length = 10296

    try:
        file = open(file_path, 'rb')
    except OSError:
        logger.error(f'No such a file or directory: {yellow}"{file_path}"{reset}'),
        end()
    with file:
        switch_file = file.read()
        file.close()

    if len(switch_file) != 5159100:
        logger.error('Invalid Format!! - Please use Switch save data')
        end()

    slot1_validation = switch_file[slot1_wrong_position:slot1_wrong_position + 10] != bytes(10)
    slot2_validation = False
    slot3_validation = False
    prev_slot_bytes = bytes(b'\xff\x8b\xa1P\xff')

    if switch_file[2525141 - 11:2525141 - 6] == prev_slot_bytes:
        slot2_validation = switch_file[2525141:2525141 + 10] != bytes(10)

    if switch_file[3698581 - 11:3698581 - 6] == prev_slot_bytes:
        slot3_validation = switch_file[3698581:3698581 + 10] != bytes(10)

    try:
        blank_file = open(blank_path, 'rb')
    except OSError:
        logger.error(f'No such a file or directory: {yellow}"{blank_path}"{reset}')
        end()
    with blank_file:
        blank = blank_file.read()
        blank_file.close()

    if len(blank) != 5159100:
        logger.error(f'Corrupt or wrong file in: {yellow}"{path(blank_path)}"{reset}')
        end()

    header = blank[:40] + switch_file[40:43 + 1] + blank[44:slot1_position]

    is_position_slot_wrong = slot1_validation or slot2_validation or slot3_validation

    check_slot1_position = slot1_wrong_position if is_position_slot_wrong else slot1_position
    check_slot2_position = slot2_wrong_position if is_position_slot_wrong else slot2_position
    check_slot3_position = slot3_wrong_position if is_position_slot_wrong else slot3_position

    new_save_data = header + switch_file[check_slot1_position:]

    # fix chat slot1
    new_save_data = fix_chat(new_save_data, switch_file, chat1_position, check_slot2_position)

    # fix chat slot2
    new_save_data = fix_chat(new_save_data, switch_file, chat2_position, check_slot3_position)

    # fix chat slot3
    new_save_data = fix_chat(new_save_data, switch_file, chat3_position, chat3_position + chat_length)

    output = open(output_path, 'wb')
    output.write(new_save_data)
    output.close()

    logger.info(f'File generated in: {yellow}"{path(output_path)}"{reset}')
    end()


def main():
    if __name__ == '__main__':
        tprint('FIX SAVE\n\n', font='tarty1')
        fix_save()


main()
