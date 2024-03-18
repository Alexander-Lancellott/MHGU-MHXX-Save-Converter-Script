from modules.utils import custom_logger, end, path
from art import *

init_logger = custom_logger(__name__)
logger = init_logger['logger']
yellow = init_logger['yellow']
reset = init_logger['reset']


def fix_chat(new_save_data, _3ds_file, slot_position, chat_position):
    chat_range = 100
    extra_chat_bytes = bytes(44)

    new_save_data += _3ds_file[slot_position:chat_position]
    for i in range(1, chat_range):
        new_save_data += _3ds_file[chat_position + (60 * (i - 1)): chat_position + (60 * i)] + extra_chat_bytes

    return new_save_data


def mhxx_to_mhgu():
    file_path = 'system'
    output_path = 'output - ( Switch )/system'
    blank_path = '../Blank_Switch_Save/system'

    initial_position = 1625244
    slot1_position = 1205364
    slot2_position = 2378801
    slot3_position = 3552241
    chat1_position = 2372861
    chat2_position = 3546301
    chat3_position = 4719741
    chat_length = 5940

    try:
        file = open(file_path, 'rb')
    except OSError:
        logger.error(f'No such a file or directory: {yellow}"{file_path}"{reset}'),
        end()
    with file:
        _3ds_file = file.read()
        file.close()

    if len(_3ds_file) != 4726152:
        logger.error("Invalid Format!! - Please use 3DS save data")
        end()

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

    new_save_data = blank[:40] + _3ds_file[4:8] + blank[44:initial_position]

    # fix chat slot1
    new_save_data = fix_chat(new_save_data, _3ds_file, slot1_position, chat1_position)

    # fix chat slot2
    new_save_data = fix_chat(new_save_data, _3ds_file, slot2_position, chat2_position)

    # fix chat slot3
    new_save_data = fix_chat(new_save_data, _3ds_file, slot3_position, chat3_position)

    new_save_data += _3ds_file[chat3_position + chat_length:]

    output = open(output_path, 'wb')
    output.write(new_save_data)
    output.close()

    logger.info(f'File generated in: {yellow}"{path(output_path)}"{reset}')
    end()


def main():
    if __name__ == '__main__':
        tprint("MHXX TO MHGU\n\n", font='tarty1')
        mhxx_to_mhgu()


main()
