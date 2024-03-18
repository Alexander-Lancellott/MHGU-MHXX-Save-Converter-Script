from modules.utils import custom_logger, end, path
from art import *

init_logger = custom_logger(__name__)
logger = init_logger['logger']
yellow = init_logger['yellow']
reset = init_logger['reset']


def fix_chat(new_save_data, switch_file, slot_position, chat_position):
    chat_range = 100
    extra_chat_bytes = 44

    new_save_data += switch_file[slot_position:chat_position]
    for i in range(1, chat_range):
        new_save_data += switch_file[chat_position + (104 * (i - 1)): chat_position + (104 * i) - extra_chat_bytes]

    return new_save_data


def mhgu_to_mhxx():
    file_path = 'system'
    output_path = 'output - ( 3DS )/system'
    blank_path = '../Blank_3DS_Save/system'

    initial_position = 1205364
    slot1_position = 1625244
    slot2_position = 2803037
    slot3_position = 3980833
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
        logger.error("Invalid Format!! - Please use Switch save data")
        end()

    try:
        blank_file = open(blank_path, 'rb')
    except OSError:
        logger.error(f'No such a file or directory: {yellow}"{blank_path}"{reset}')
        end()
    with blank_file:
        blank = blank_file.read()
        blank_file.close()

    if len(blank) != 4726152:
        logger.error(f'Corrupt or wrong file in: {yellow}"{path(blank_path)}"{reset}')
        end()

    new_save_data = blank[:4] + switch_file[40:44] + blank[8:initial_position]

    # fix chat slot1
    new_save_data = fix_chat(new_save_data, switch_file, slot1_position, chat1_position)

    # fix chat slot2
    new_save_data = fix_chat(new_save_data, switch_file, slot2_position, chat2_position)

    # fix chat slot3
    new_save_data = fix_chat(new_save_data, switch_file, slot3_position, chat3_position)

    new_save_data += switch_file[chat3_position + chat_length:]

    output = open(output_path, 'wb')
    output.write(new_save_data)
    output.close()

    logger.info(f'File generated in: {yellow}"{path(output_path)}"{reset}')
    end()


def main():
    if __name__ == '__main__':
        tprint('MHGU TO MHXX\n\n', font='tarty1')
        mhgu_to_mhxx()


main()
