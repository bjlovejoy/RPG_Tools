"""
Helpful functions to be used throughout the other classes.
"""
from time import strftime
from os import system, name
from random import randint, choice
from textwrap import fill

from colorama import Fore, Back, Style
from art import text2art
#TODO: maybe provide support for sound for menus

ascii_art = text2art

def clear_screen():
    if name == 'nt':    # for windows
        _ = system('cls')
    else:    # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

def display_title(text:str, fore:str, back:str, text_to_proceed:str="Press ENTER to START"):
    """
    Colors: black, red, green, yellow, blue, magenta, cyan, white, reset
    """
    fore_colors = {"black": Fore.BLACK, "red": Fore.RED, "green": Fore.GREEN,
                   "blue": Fore.BLUE, "yellow": Fore.YELLOW, "magenta": Fore.MAGENTA,
                   "cyan": Fore.CYAN, "white": Fore.WHITE, "normal": Fore.RESET}
    back_colors = {"black": Back.BLACK, "red": Back.RED, "green": Back.GREEN,
                   "blue": Back.BLUE, "yellow": Back.YELLOW, "magenta": Back.MAGENTA,
                   "cyan": Back.CYAN, "white": Back.WHITE, "normal": Back.RESET}
    print(fore_colors[fore] + back_colors[back])
    clear_screen()
    print(fore_colors[fore] + back_colors[back] + text + '\n')
    input(text_to_proceed)
    print(Style.RESET_ALL, end="", flush=True)
    clear_screen()

def display(text:str, source:str, wrap_text=True):
    """
    Sources: warning (red), settings (cyan), narrator (green), list (yellow), inventory (blue), user (white)
    """
    color = str()
    if source == "narrator":
        color = Fore.GREEN
    elif source == "warning":
        color = Fore.RED
    elif source == "settings":
        color = Fore.CYAN
    elif source == "list":
        color = Fore.YELLOW
    elif source == "inventory":
        color = Fore.BLUE

    if wrap_text:
        text = fill(text, 70)
    print(color + text)
    print(Style.RESET_ALL, end="", flush=True)

def write_to_log(text="", new_session=False):
    if new_session:
        text = '\n\n' + strftime('%a. %b %d, %Y %T') + '\n'
        for _ in range(50):
            text += '-'
        text += '\n'
    with open('RPG_user_input.log', 'a') as log:
        log.write(text + '\n')

def read_input(separated=True):
    """
    Collect input from player and convert string into list of lowercase words
    """
    user_input = input(Fore.WHITE + ">>> ").lower()

    write_to_log(user_input)

    if separated:
        return user_input.split()
    else:
        return user_input

def read_number_input(low, high, initial_text="", error_text=""):
    """
    Collect input from player asking to choose a number between 2 numbers.
    Asserts that the input is a number and returns the selected number.
    """
    if initial_text:
        display(initial_text, "narrator")
    try:
        selection = int(read_input(False))
    except ValueError:
        selection = 0
    while selection < low or selection > high:
        if error_text:
            display(error_text, "warning")
        try:
            selection = int(read_input(False))
        except ValueError:
            selection = 0
    return selection

def random_selection(seq:list):
    return choice(seq)
