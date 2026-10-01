#Membership operators are used to see if a variable or value is found in a sequence like (string, list, tuple etc)

#1) in and 2) not in

name = input("Enter Name: ")
word = "lol"

if word in name:
    print("Yes!")

if word not in name:
    print("Nope Not Found!")

#-------------------------------------------------
#For List
listi = [10,20,30,40,50,60]
num = int(input("Enter A Num: "))

if num in listi:
    print("Yep It Exists!")

#-------------------------------------------------
#for Dictionary
grades = {
    "User": "A",
    "User2": "B",
    "User3": "C",
    "User4": "D"
}

student = input("Enter Name: ")

if student in grades: # in grades here checks for key not value
    print(f"Your Grades Are:{grades[student]}")