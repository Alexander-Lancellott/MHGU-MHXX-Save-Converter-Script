import os
import sys
import time
import readchar
import logging
from colorama import Fore

blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
reset = Fore.RESET


class CustomFormatter(logging.Formatter):
    format_info = f'- [{green}%(levelname)s{reset}] %(message)s'
    format_error = f'- [{red}%(levelname)s{reset}] %(message)s'

    FORMATS = {
        logging.INFO: f'{blue}%(asctime)s{reset} {format_info}',
        logging.ERROR: f'{blue}%(asctime)s{reset} {format_error}',
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(log_fmt, date_fmt)
        return formatter.format(record)


def path(file_path):
    relative_dir = os.path.dirname(file_path)
    absolute_dir = os.path.dirname(os.path.abspath(file_path))
    return absolute_dir if file_path.split('/')[0] == '..' else relative_dir


def end():
    time.sleep(1)
    print('\nPress Any Key To Exit')
    readchar.readchar()
    sys.exit()


def custom_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)
    return dict(logger=logger, yellow=yellow, reset=reset)
