
from csv_reader import csv_reader
import random

def single_char_input(prompt=""):
    """
    Function to request a single input
    """
    while True:			
        try:
            user_input = input(prompt)                                              #requests input from user

            while len(user_input) != 1 or not user_input.isalpha():                 #keeps prompting if invalid input
                user_input = input("Please enter a valid single character: ")
        except ValueError:
            continue
        else:
            break
    return user_input




def Round(dictionary):

        secret_word = random.choice(dictionary)
        turns = 7
        guess = ''
        guess_display = ""
        for char in secret_word:
            if char != " ":
                guess_display += "_"
            else:
                guess_display += " "

    
        print(guess_display)

        guess_history = []
        while turns > 0:    
           
    

            print(f"guess history:{guess_history}")   
            guess = single_char_input("Guess a chracter: ")
            print("\n")
            if guess not in guess_history:
                guess_history.append(guess)
                if guess in secret_word:



                    guess_display = list(guess_display)
                    for i in range(len(secret_word)):
                        if guess == secret_word[i]:
                            guess_display[i] = guess
                    guess_display = "".join(guess_display)




                else:
                    turns -= 1
                    print("WRONG!")
                    print(f"you have {turns} turns left")
            else:
                print("You have already guessed this")
                print(f"guess history:{guess_history}")


            #check if you guessed all the characters
            if '_' not in guess_display:
                break

            print("***************************************")
            print(guess_display)
            

        if turns <=0:
            print("You lose")
            print(f"The word was {secret_word}")
        else:
            print("You win")
   
