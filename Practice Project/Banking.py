#Python Banking Program
import time

balance = 0
print("---------------------------------------------")
print("-------------Welcome To The Bank-------------")
print("---------------------------------------------")


def show_balance(balancee):
    print(f"Your Current Balance Is ${balancee}")
    print()

def deposite():
    increment = float(input("How Much Would You Like To Deposite: "))
    return increment

def withdraw():
    decrement = float(input("How Much Would You Like To Withdraw: "))
    return decrement


while balance>=0:
    print()
    print("1) Show Balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Exit")
    print()

    choice = int(input("Enter A Choice (1-4): "))

    if choice == 1:
        show_balance(balance)
    elif choice == 2:
        bal = deposite()
        balance += bal
    elif choice == 3:
        dec = withdraw()
        balance -= dec
    elif choice == 4:
        print("Thank-You For Using Our Services")
        time.sleep(2)
        break
    else:
        print("Please Enter A Valid Choice")

