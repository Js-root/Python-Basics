# Just A Slot Machine Lol, (Dont Gamble Kids!💀)

import time
import random

print("===============================================================")
print("------------------Welcome To The Slot Machine------------------")
print("Symbols- 🍎🍋🍌⭐🔔")
print("===============================================================")

symbols = ["🍎", "🍋", "🍌", "⭐", "🔔"]
balance = 100

while True:
    if balance <= 0:
        print("Not Enough Balance!")
        time.sleep(2)
        break

    wanna_play = input("Do You Wanna Continue? (Y/N): ")

    if wanna_play.lower() == "n":
        break

    print(f"\nYour Current Balance is: ${balance}")
    bet = float(input("How Much Would You Bet?: "))

    if bet <= 0:
        print("Bet must be greater than 0!")
        continue

    if bet > balance:
        print("Not Enough Balance!")
        continue

    balance -= bet

    print("Spinning........")
    time.sleep(2)

    ch1 = random.choice(symbols)
    ch2 = random.choice(symbols)
    ch3 = random.choice(symbols)

    print(ch1, end=" ")
    print(ch2, end=" ")
    print(ch3)

    if ch1 == ch2 and ch2 == ch3:
        balance += bet * 2
        print(f"🎉 JACKPOT! You won ${bet * 2}")

    elif ch1 == ch2 or ch2 == ch3 or ch1 == ch3:
        balance += (bet * 1.2)
        print(f"✨ Two matching symbols! You won ${bet * 1.2}")

    else:
        print(f"💀 You lost ${bet}")
