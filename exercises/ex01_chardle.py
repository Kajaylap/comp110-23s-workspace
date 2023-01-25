"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730418782"

five_char_word = input("Enter a 5-character word: ")

if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_char = input("Enter a single character: ")
    if len(single_char) != 1:
        print("Error: Word must contain 5 characters")
        exit()


search_prompt = print("Searching for", single_char, "in", five_char_word)

# printing out correct index
zero = five_char_word[0] == single_char
if zero:
    print(single_char, "found at index 0")

one = five_char_word[1] == single_char
if one:
    print(single_char, "found at index 1")

two = five_char_word[2] == single_char
if two:
    print(single_char, "found at index 2")

three = five_char_word[3] == single_char
if three:
    print(single_char, "found at index 3")

four = five_char_word[4] == single_char
if four:
    print(single_char, "found at index 4")


if zero:
    zero_instance = int(1)

else:
    zero_instance = int(0)


if one:
    one_instance = int(1)

else:
    one_instance = int(0)


if two:
    two_instance = int(1)

else:
    two_instance = int(0)
  

if three:
    three_instance = int(1)

else:
    three_instance = int(0)


if four:
    four_instance = int(1)

else:
    four_instance = int(0)


sum = int(zero_instance + one_instance + two_instance + three_instance + four_instance)

if sum == 0:
    print("No instances of", single_char, "found in", five_char_word)

elif sum == 1:
    print(sum, "instance of", single_char, "found in", five_char_word)

else:
    sum > 1
    print(sum, "instances of", single_char, "found in", five_char_word)
