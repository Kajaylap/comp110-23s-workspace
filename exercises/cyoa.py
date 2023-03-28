"""EX06 - Choose your own Adventure. A number guessing game that tracks attempts until guessed correctly."""

__author__ = "730418782"

import random
points: int = 0
player: str = ""
NUMBER = int(random.randint(0,100))
HAPPY_FACE = "\U0001F60A"
SAD_FACE = "\U0001F641"

def main() -> None:
    greet()
    yes_or_no = ask()
    guessing(yes_or_no)


def greet() -> None:
    global player
    player = input("Hi! What is your name? ")
    print(f"Welcome {player} to Guess the Mystery Number!")

def ask() -> int:
    global player
    global start_or_exit
    start_or_exit = int(input("Would you like to start playing, input 1 for Yes or 2 for No? " ))
    if start_or_exit == int(1):
        return int(1) 
    if start_or_exit == int(2):
        return int(2) 
    

def guessing(playing: int) -> int:
    global points
    global player
    global NUMBER
    if playing == int(1):
        print("Great! Lets start playing!")
        guessed_number = int(input("Input your guess between 0-100 "))
        guess_attempt = True
        while guess_attempt:
            points += 1
            if int(guessed_number) == int(NUMBER):
                print(f"Congrats! You guessed the correct number {HAPPY_FACE}")
                print(f"Your total attempts was {points}")
                guess_attempt = False
            else:
                while int(guessed_number) != int(NUMBER):
                    points += 1
                    if int(guessed_number) < int(NUMBER):
                        print(f"Sorry, try again! Guess is too low {SAD_FACE} attempts: {points}")
                        guessed_number = int(input("Input your guess between 0-100 "))
                    else:
                        print(f"Sorry, try again! Guess is too high {SAD_FACE} attempts: {points}")
                        guessed_number = int(input("Input your guess between 0-100 "))
    if playing == int(2):
        return print(f"Bye-bye {player}! {HAPPY_FACE} Thank you for playing! Your total attempts was {points}")
        

if __name__ == "__main__":
    main()