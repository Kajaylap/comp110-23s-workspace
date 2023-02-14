"""EX02 - one shot Wordle."""

__author__ = "730418782"

SECRET_WORD = "python"
len_secret_word: int = len(SECRET_WORD)
guess = input(f"What is your { len_secret_word }-letter guess? ")
guessing: bool = True
guess_index: int = 0
alt_indices: int = 0
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
result: str = "" 
while guessing:
    while len(guess) != len_secret_word: # the input doesn't equal the secret word
        print("That was not 6 letters! Try again: ")
        guess = input(f"What is your { len_secret_word }-letter guess? ")
    while len_secret_word > guess_index: # the while loops repeat until 
        # guess_index is greater than the len of the secret word
        if guess[guess_index] == SECRET_WORD[guess_index]:
            result = result + green_box #concatenating a string for the boxes
        else:
            guess_character: bool = False
            while guess_character:
                while len_secret_word > alt_indices:
                    if guess[alt_indices] == SECRET_WORD[alt_indices]:
                        guess_character = True
                    else:
                        result = result + white_box
                        alt_indices = alt_indices + 1
            result = result + yellow_box
            alt_indices = alt_indices + 1
            guessing = False
        print(result)

