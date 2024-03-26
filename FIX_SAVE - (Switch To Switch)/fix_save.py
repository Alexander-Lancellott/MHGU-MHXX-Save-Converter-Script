import os
import sys
import time
from modules.utils import custom_logger, end, path
from art import *


init_logger = custom_logger(__name__)
logger = init_logger['logger']
yellow = init_logger['yellow']
reset = init_logger['reset']


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    tprint('FIX SAVE\n\n', font='tarty1')


def custom_input():
    choice = "Wrong"

    while not choice.isdigit() or int(choice) > 2 or int(choice) == 0:
        print(
            'What do you want to do with the chat menu?\n\n'
            f'[{yellow}1{reset}] - Try to recover it - (Mostly recommended if you didn\'t edit the chats in MHGU)\n\n'
            f'[{yellow}2{reset}] - Replace it with the English version of MHGU\n'
        )

        try:
            choice = input('Enter the number of the option: ')
        except KeyboardInterrupt:
            sys.exit()

        print('')

        if not choice.isdigit() or int(choice) > 2 or int(choice) == 0:
            logger.error(f'{yellow}"{choice}"{reset} is not an allowed option, try again')
            time.sleep(2)
            clear_screen()
        else:
            return int(choice)


def fix_chat(
        new_save_data,
        switch_file,
        chat_position,
        current_slot_position,
        slot_position,
        is_position_slot_wrong,
        slot_wrong_position,
        option
):
    chat_path = 'bin/chat'
    chat_length = 10296
    chat_range = 100
    extra_chat_bytes = bytes(44)
    position_difference = slot_position - slot_wrong_position if is_position_slot_wrong else 0
    new_save_data += switch_file[current_slot_position:(chat_position - position_difference)]

    if option == 1:
        for i in range(1, chat_range):
            new_save_data += (
                switch_file[
                    (chat_position - position_difference) + (60 * (i - 1)):
                    (chat_position - position_difference) + (60 * i)
                ] + extra_chat_bytes
            )

        return new_save_data
    else:
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

        return new_save_data + chat


def fix_save():
    file_path = 'system'
    output_path = 'output - (Switch)/system'
    blank_path = '../Blank_Switch_Save/system'

    slot_positions = [1625244, 2803037, 3980833]
    slot_wrong_positions = [1205400, 2378837, 3552277]
    chat_positions = [2792741, 3970537, 5148333]
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

    slot1_validation = switch_file[slot_wrong_positions[0]:slot_wrong_positions[0] + 10] != bytes(10)
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

    is_position_slot_wrong = slot1_validation or slot2_validation or slot3_validation

    check_slot_positions = list(
        map(
            lambda position, wrong_position: wrong_position if is_position_slot_wrong else position,
            slot_positions,
            slot_wrong_positions
        )
    )

    new_save_data = blank[:40] + switch_file[40:43 + 1] + blank[44:slot_positions[0]]

    option = custom_input()

    # fix chats
    for i in range(len(chat_positions)):
        new_save_data = fix_chat(
            new_save_data,
            switch_file,
            chat_positions[i],
            check_slot_positions[i],
            slot_positions[i],
            is_position_slot_wrong,
            slot_wrong_positions[i],
            option
        )

    new_save_data += switch_file[chat_positions[2] + chat_length:]

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
