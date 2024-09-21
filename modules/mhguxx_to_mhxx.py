from art import tprint
from modules.utils import custom_logger, keyHandler, path, get_file, absolute_path

init_logger = custom_logger(__name__)
logger = init_logger['logger']
yellow = init_logger['yellow']
reset = init_logger['reset']


def fix_chat(new_save_data, switch_file, slot_position, chat_position):
    chat_range = 100
    extra_chat_bytes = 44

    new_save_data += switch_file[slot_position:chat_position]
    for i in range(1, chat_range):
        new_save_data += switch_file[
            chat_position + (104 * (i - 1)): chat_position + (104 * i) - extra_chat_bytes
        ]

    return new_save_data


def mhguxx_to_mhxx():
    tprint('MHGU-XX TO MHXX\n\n', font='tarty1')

    file_path = 'MHGU-XX_TO_MHXX - (Switch To 3DS)/system'
    output_path = 'MHGU-XX_TO_MHXX - (Switch To 3DS)/output - (3DS)/system'
    blank_path = 'Blank_3DS_Save/system'

    initial_position = 1205364
    slot_positions = [1625244, 2803037, 3980833]
    chat_positions = [2792741, 3970537, 5148333]
    chat_length = 10296

    switch_file = get_file(file_path, logger)

    if not switch_file:
        return

    if len(switch_file) not in (5159100, 4726188):
        logger.error('Invalid Format!! - Please use Switch save data')
        return keyHandler().run()

    blank = get_file(blank_path, logger)

    if not blank:
        return

    if len(blank) != 4726152:
        logger.error('Corrupt or wrong file in: %s"%s"%s', yellow, path(blank_path), reset)
        return keyHandler().run()

    new_save_data = blank[:4] + switch_file[40:44] + blank[8:initial_position]

    if len(switch_file) == 5159100:
        # fix chat
        for i, chat_position in enumerate(chat_positions):
            new_save_data = fix_chat(new_save_data, switch_file, slot_positions[i], chat_position)

        new_save_data += switch_file[chat_positions[2] + chat_length:]
    else:
        new_save_data += switch_file[1205400:]

    output = open(absolute_path(output_path), 'wb')
    output.write(new_save_data)
    output.close()

    logger.info('File generated in: %s"%s"%s', yellow, path(output_path), reset)
    keyHandler().run()


if __name__ == '__main__':
    mhguxx_to_mhxx()
