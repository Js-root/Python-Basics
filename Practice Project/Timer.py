#We made a timer in this practice project 

import time 

print("Welcome to the timer clock: ")

timer = int(input("Enter Timer Limit: "))

for i in range(timer,0,-1):
    seconds = i%60
    minutes = int(i / 60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Booommmm!!!!, Wakey Wakey")