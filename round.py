
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


#ASCII art from chrishorton github page
#https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

def get_art(index):
    HANGMANPICS = ['''
  
    
      YOU ARE SAFE!
                   
      
      
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    HANGMANPICS.reverse()
    return HANGMANPICS[index]





def Round(dictionary):

        secret_word = random.choice(dictionary).lower()
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
            guess = single_char_input("Guess a chracter: ").lower()
            print("\n")
            
            if guess not in guess_history:
                guess_history.append(guess)
                if guess in secret_word:



                    guess_display = list(guess_display)
                    for i in range(len(secret_word)):
                        if guess == secret_word[i]:
                            guess_display[i] = guess
                    guess_display = "".join(guess_display)
                    print(get_art(turns))




                else:
                    turns -=1
                    print(get_art(turns))
                    print(f"Wrong! you have {turns} turns left")
            else:
                print(get_art(turns))
                print("You have already guessed this, try again.")
                
    

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
   
