#For loop = Executes a block of code a fixed number of times

name = "someName"

for i in range(1,11):#Range Function defines the range (11 is not counted)
    print(i)

for i in reversed(range(1,11)):#Reversed function Reverses like from 10-1
    print(i)

for i in range (1,11,2): #2 here means that we skip 2 numbers each iteration
    print(i)

for i in name:#Prints the string one char at a time 
    print(i)

for i in range(1,15):
    if i == 5:
        continue #Skips the current iteration

    elif i == 12:
        break #Gets out of loop

    else:
        print(i)
