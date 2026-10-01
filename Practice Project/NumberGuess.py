#In this practice project we are going to create a number guessing game using random() function

import random

print("-----------------Welcome To The Game-----------------")

attempts = 5
low = 1
high = 100
number = random.randint(low,high)

while not attempts == 0:
    guess = int(input("Enter A Guess: (1-100) "))
    attempts -=1

    if guess > high or guess < low:
        print("That's Not A Range..")
        print(f"{attempts} attempts remains ")
        
    elif number == guess:
        print("You Won!")
        print(f"It took you {attempts} attempts")
        break

    elif guess > number:
        print("Go Low!")
        print(f"{attempts} attempts remains ")

    elif guess < number:
        print("Go High!")
        print(f"{attempts} attempts remains ")

if attempts == 0:
    print("You Lose!! Better Luck Next Time")
    print(f"The Number Was {number}")