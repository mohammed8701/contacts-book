import sys
import main
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def quit_app():
    print("\n")
    clear()
    print("\nPlease come again!")
    sys.exit()


def empty_line():
    print('\n')

def print_invalid_option():
        print("\nSorry, that's not an option! Please try again.\n")
        
error_message = "is not an available options"

def start_again():
    while True:
        user_choice = input("\nMain Menu: '1'\nQuit: '0'\n")
        if user_choice == "1":
            main.main()
            False
        elif user_choice == "0":
            quit_app()
            False
        else:
            clear()
            print(user_choice, error_message)
            print("Error: please input either '0' or '1'")


def index_selector():
    