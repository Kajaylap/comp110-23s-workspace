"""EX02 - one shot Wordle."""

__author__ = "730418782"

guess = input("What is your 6-letter guess? ")
SECRET_WORD = "python"
guessing: bool = True
guess_index: int = 0
guess_character: bool = False
alt_indices: int = 0
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box = str = "\U0001F7E8"
while guessing:
    if len(guess) != len(SECRET_WORD): # the input doesn't equal the secret word
        print("That was not 6 letters! Try again: ")
        guess = input("What is your 6-letter guess? ")
    else:
        while len(SECRET_WORD) > guess_index: # the while loops repeat until 
            # guess_index is greater than the len of the secret word
            if guess[guess_index] == SECRET_WORD[guess_index]:
                print(green_box)
            else:
                while guess_character:
                    if len(SECRET_WORD) > guess_character:
                        if guess[alt_indices] == SECRET_WORD[alt_indices]:
                            guess_character = True
                        alt_indices = alt_indices + 1
                    print(yellow_box)
                print(white_box)
            guess_index = guess_index + 1
        
# Need to make while loop false to exit

