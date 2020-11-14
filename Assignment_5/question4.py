'''
Create a Python project to guess a number that has randomly selected.
Hint: you could use random module to generate a number from 0-100.

'''
import random
number = random.randrange(0,100)
guessCheck = "wrong"
print("Welcome to Number Guess")

while guessCheck == "wrong":
    response = input("Please input a number between 0 and 100 : ")
    try:
        val = int(response)
    except ValueError:
        print("This is not a valid integer. Please try again")
        continue
    if val < number:
        print("This is lower than actual number. Please try again.")
    elif val > number:
        print("This is higher than actual number. Please try again.")
    else:
        print("This is the correct number")
        guessCheck = "correct"

print("Thank you for playing Number Guess. See you again")