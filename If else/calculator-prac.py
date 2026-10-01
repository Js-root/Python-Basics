import time
#We will be making a calculator using if else in this practice project :)

print("Welcome To The Calculator : ")

choice = input("What Would You Like To Do (+,-,*,/)? : ")
num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))

if choice == "+":
    result = num1 + num2
    print(result)
elif choice == "-":
    result = num1 - num2
    print(result)
elif choice == "*":
    result = num1 * num2
    print(result)
elif choice == "/":
    result = num1 / num2
    print(result)
else:
    print("Nahh man that aint supported here :( ")
    print("But But But.....Here's Every Operation lol")
    print("Calculating........")
    time.sleep(3)
    res1 = num1 + num2
    res2 = num1 - num2
    res3 = num1 * num2
    res4 = num1 / num2
    print(res1, res2, res3, res4)