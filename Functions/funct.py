#Functions are reusable block of codes that can be used multiple times
#Return keyword is used to return a value to the caller from a function
#def keyword is used to make function in python

def name(first,last):
    first = first.capitalize()
    last = last.capitalize()

    return (first+ " " + last)

firstname = input("Enter First name: ")
lastname = input("Enter Last name: ")

print(name(firstname,lastname))