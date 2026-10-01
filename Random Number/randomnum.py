#Here will talk about random function used to create random numbers 

import random

car = ("Lambo", "BMW", "Ferrari", "Byd", "Jaguar")
fruits = ["banana", "orange", "apple", "cherries", "grapes"]

print(random.randint(1,10)) #Returns a random number between 1,10
print(random.random()) #Returns a random num between 0-1

print(random.choice(car))#chooses random string from the tupple

random.shuffle(fruits)#shuffles the list randomly
print(fruits)

