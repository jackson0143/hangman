class Round:
    def __init__(self, secret_word, dictionary) -> None:
        self.secret_word = secret_word
        self.dictionary = dictionary

        turns = 7
        guess = ''
        guess_display = ""
        for _ in range(len(secret_word)):
            guess_display += "_"

        print(guess_display)


        
        while turns > 0:            
            guess = input("guess a character")
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
                print("You win")


                
            print(guess_display)
        print("You lose")
   
test = Round('secret', 'secret')