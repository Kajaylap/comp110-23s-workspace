"""EX02 - one shot Wordle."""

__author__ = "730418782"

guess = input("What is your 6-letter guess? ")
secret_word = "python"
guess_index: int = 0
White_box: str = "\U00002B1C"
Green_box: str = "\U0001F7E9"

while guess:
    if len(guess) != len(secret_word):
        print("That was not 6 letters! Try again: ")
        guess = input("What is your 6-letter guess? ")
    while len(secret_word) > guess_index:
        if guess[guess_index] == secret_word[guess_index]:
            Correct = print(Green_box)
            guess_index = guess_index + 1
            if Correct:
                print("Woo! You got it!")
                guess = input("What is your 6-letter guess? ")
        else:
            Wrong = print(White_box)
            print("Not quite. Play again soon!")
            guess_index = guess_index + 1
            guess = input("What is your 6-letter guess? ")
