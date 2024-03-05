
from csv_reader import csv_reader
import random
class Round:
    def __init__(self, dictionary) -> None:
        
        self.dictionary = dictionary
        secret_word = random.choice(dictionary)
        


        

        turns = 7
        guess = ''
        guess_display = ""
        for char in secret_word:
            if char != " ":
                guess_display += "_"
            else:
                guess_display +=" "

        print(guess_display)


        
        while turns > 0:    
            print("Guess a chracter: ")        
            guess = input()
            if guess in secret_word:
                guess_display = list(guess_display)
                for i in range(len(secret_word)):
                    if guess == secret_word[i]:
                        guess_display[i] = guess
                guess_display = "".join(guess_display)


            else:
                turns -= 1
                print(f"you have {turns} turns left")


            #check if you guessed all the characters
            if '_' not in guess_display:
                break

            print(guess_display)


        if turns <=0:
            print("You lose")
            print(f"The word was {secret_word}")
        else:
            print("You win")
   

dictionary = csv_reader("fruits.csv")
print(dictionary)
test = Round(dictionary)