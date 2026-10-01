#This is a compound interest calculator
#User can give info and get the total compound interest 

principle = 0
rate = 0
time = 0

#While loop for principle
while principle<=0:
    principle = float(input("Enter Principle: "))

    if principle<= 0:
        print("It Cannot be 0 or less")

#While loop for rate 
while rate<= 0:
    rate = float(input("Enter Interest Rate: "))

    if rate <= 0:
        print("Rate Cannot be 0 or less")

#While loop for time
while time<= 0:
    time = float(input("Enter Time: "))

    if time <= 0:
        print("Time Cannot be 0 or less")

#Formula for calculating 

final = principle * pow((1+rate/100),time)
print(f"Your Compound Interest For {time} years would be ${final:.3f}")