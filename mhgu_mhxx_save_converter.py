from art import tprint
from modules.utils import custom_logger, clear, custom_input
from modules.fix_save import fix_save
from modules.mhxx_to_mhguxx import mhxx_to_mhguxx
from modules.mhguxx_to_mhxx import mhguxx_to_mhxx

init_logger = custom_logger(__name__)
logger = init_logger["logger"]
yellow = init_logger["yellow"]
reset = init_logger["reset"]


def clear_screen():
    clear()
    tprint("SAVE CONVERTER\n\n", font="tarty1")


if __name__ == "__main__":
    while True:
        clear_screen()
        msg = (
            "Enter the number of the option you want to use:\n\n"
            f"[{yellow}1{reset}] - EXIT\n"
            f"[{yellow}2{reset}] - FIX SAVE\n"
            f"[{yellow}3{reset}] - MHGU/MHXX TO MHXX - (Switch To 3DS)\n"
            f"[{yellow}4{reset}] - MHXX TO MHGU/MHXX - (3DS To Switch)\n"
        )
        option = custom_input(msg, "> ", 4, logger, clear_screen)
        if option == 1:
            break
        elif option == 2:
            clear()
            fix_save()
        elif option == 3:
            clear()
            mhguxx_to_mhxx()
        else:
            clear()
            mhxx_to_mhguxx()
