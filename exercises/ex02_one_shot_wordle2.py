"""EX02 - one shot Wordle."""

__author__ = "730418782"

SECRET_WORD = "python"
len_secret_word: int = len(SECRET_WORD)
guess = input(f"What is your { len_secret_word }-letter guess? ")
guessing: bool = True

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
guess_index: int = 0

result: str = ""


while guessing:
    while len(guess) != len_secret_word:  #the input doesn't equal the secret word
        print("That was not 6 letters! Try again: ")
        guess = input(f"What is your { len_secret_word }-letter guess? ")

    while len_secret_word > guess_index:   #the while loops repeat until guess_index is greater than the len of the secret word
        if guess[guess_index] == SECRET_WORD[guess_index]:
            result = result + green_box  #concatenating a string for the boxes  
            guess_index = guess_index + int(1)
        else:
            guess_character: bool = False
            alt_indices: int = 0
            while not guess_character and alt_indices < len_secret_word:
                    if guess[guess_index] == SECRET_WORD[alt_indices]:
                        guess_character = True
                    else:
                        alt_indices = alt_indices + 1
            if guess_character == True:
                result = result + yellow_box
            else:
                result = result + white_box
            guess_index = guess_index + int(1)
    guessing = False
print(result)

result_text: bool = True
result_index: int = 0
while result_text:
       result_index = result_index + 1
       if result[result_index] == green_box:
            print("Woo! You got it!")
            result_text = False
       else:
           print("Not quite. Play again soon!")
           result_text = False
