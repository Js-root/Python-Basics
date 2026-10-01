#In this practice project will use dictionary to create a menu

menu = {
    "Burger": 5.99,
    "Pizza": 8.49,
    "Fries": 3.49,
    "Hot Dog": 4.99,
    "Ice Cream": 2.99
}

cart = []
total = 0

print("---------------------Menu---------------------")
for key,value in menu.items():
    print(f"{key:10}: ${value}")
print("----------------------------------------------")

while True:
    food = input("Enter Food: (q To exit)")
    food = food.title() #title makes first letter uppercase

    if food == "Q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

for i in cart:
    total += menu.get(i)

print(f"Your Total Is: {total}")