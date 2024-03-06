from csv_reader import csv_reader

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
        Round()