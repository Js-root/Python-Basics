#While loops executes until the condition remains true
#-------------------------------------------------------------
name = input("Enter Name: ")

while not name == "admin":
     print("Nope you are not admin :( ")
     name = input("Enter Name: ")

print("Welcome Admin")
#-------------------------------------------------------------
#-------------------------------------------------------------

#-------------------------------------------------------------
#Just A Smollll Practice (You Can ignore this if you want lol)👇
#-------------------------------------------------------------

num = int(input("Enter Number B/w 0-10: "))

while not (num <10 and num>0):
     print("Between 0-10 buddy")
     num = int(input("Enter Number B/w 0-10: "))

print(f"Your Number is {num}")

#-------------------------------------------------------------
#-------------------------------------------------------------

food = input("Enter A Food: (Press Q to quit)")
food = food.lower()

while not food == "q":
     print("Alright Keep On Going")
     food = input("Enter A Food: (Press Q to quit)")
     food = food.lower()

print("You Quit")
#-------------------------------------------------------------