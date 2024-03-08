from csv_reader import csv_reader
from round import Round

def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input 
    can also be restricted to a set of integers.

    Arguments:
        - prompt: String representing the message to display for input
        - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:                                 
        user_input = input(prompt)                                    #request user input and keeps prompting until valid input is received   
        try:
            int_user_input = int(user_input)                            
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_user_input in restricted_to:
            break
    return int_user_input


def display_main_menu():                                                                #main menu printing
    print("--- Main Menu ---")                                  
    print("1. Play game")
    print("2. Exit")

def main():
    print("WELCOME TO THE MINI-HANGMAN GAME")
    print("")

    game_count = 0
    print(f"Your total game sessions:{game_count}")

    display_main_menu()
    choice = int_input("Please choose an option: ", restricted_to=[1,2])
    print("")
    if choice == 1:
        dictionary = csv_reader("fruits.csv")
        Round(dictionary)

    elif choice == 2:

        print("Thanks for playing :)")
        exit()

if __name__ == "__main__":
    main()