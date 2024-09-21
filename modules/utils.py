import os
import sys
import time
import logging
from typing import Callable
from colorama import Fore
from sshkeyboard import listen_keyboard, stop_listening

BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET


class CustomFormatter(logging.Formatter):
    format_info = f'- [{GREEN}%(levelname)s{RESET}] %(message)s'
    format_error = f'- [{RED}%(levelname)s{RESET}] %(message)s'

    FORMATS = {
        logging.INFO: f'{BLUE}%(asctime)s{RESET} {format_info}',
        logging.ERROR: f'{BLUE}%(asctime)s{RESET} {format_error}',
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(log_fmt, date_fmt)
        return formatter.format(record)


def absolute_path(file_path: str = ""):
    return os.path.abspath(file_path).replace("\\modules", "")


def path(file_path: str):
    relative_dir = os.path.dirname(file_path)
    absolute_dir = os.path.dirname(os.path.abspath(file_path))
    return absolute_dir if file_path.split('/')[0] == '..' else relative_dir


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import termios  # for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


class keyHandler:
    def __init__(self):
        self.exit_flag = False

    def press(self, key):
        if key == 'r':
            stop_listening()
        else:
            stop_listening()
            self.exit_flag = True

    def run(self):
        time.sleep(1)
        print(f'\nPress {YELLOW}"R"{RESET} to return to the main menu or any other key to exit')

        listen_keyboard(on_press=self.press)

        if self.exit_flag:
            sys.exit()
        else:
            return


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_file(file_path: str, logger: logging.Logger):
    try:
        file = open(absolute_path(file_path), 'rb')
    except OSError:
        logger.error('No such a file or directory: %s"%s"%s', YELLOW, file_path, RESET)
        return keyHandler().run()
    with file:
        new_file = file.read()
        file.close()
    return new_file


def custom_input(
    msg: str,
    prompt: str,
    max_options: int,
    logger: logging.Logger,
    callback: Callable[..., None] = None,
    args: dict = ()
):
    choice = "Wrong"

    while not choice.isdigit() or int(choice) > max_options or int(choice) == 0:
        print(msg)

        try:
            flush_input()
            choice = input(prompt)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        print('')

        if not choice.isdigit() or int(choice) > max_options or int(choice) == 0:
            logger.error('%s"%s"%s is not an allowed option, try again', YELLOW, choice, RESET)
            time.sleep(2)
            if callback is not None:
                callback(*args)
        else:
            return int(choice)


def custom_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)
    return dict(logger=logger, yellow=YELLOW, reset=RESET)
