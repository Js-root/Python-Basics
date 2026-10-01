import time 
#In This We Will Try To Make A shopping cart with user input 

print("WELCOME TO THE CART:")

item = input("What Would You Like To Buy? : ")
price = float(input("What Is The Price: "))
quantity = int(input("What's The Quantity: "))

print("Calculating Total", end="")
time.sleep(1)
print(".", end="")#end keyword lets word below it to be printed in same line (run and see :) 
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".")


print(f"You Bought {quantity} {item}")
print(f"Your Total Is : ${price * quantity}")