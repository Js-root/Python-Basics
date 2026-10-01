#Creating A Madlibs Game
#A Mad Libs game is a simple word game where the computer asks you for random types of words—like a noun, adjective, verb, or name—and then puts those words into a funny story

import time
print("Welcome To Madlibs Game")

name = input("Enter A Name: ")
animal = input("Enter An Animal: ")
adjective = input("Enter An Adjective: ")
verb = input("Enter A Verb: ")

time.sleep(2)
print("Creating Story......")

print(f"One Day {name} Was Going Home and saw a {adjective} {animal}, Watching This {name} Became {adjective} and Started to {verb}")