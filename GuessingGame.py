import random

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
integer = random.choice(numberlist)
chances = 0

guess = input("Guess a number between 1 and 10")

if guess == integer:
    print("That's right!")
elif guess != integer:
    chances = chances + 1

if chances > 4:
    print("You lose! Try again.")
  
