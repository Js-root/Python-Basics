#This is a shopping cart practice project

print("---------Welcome To The Cart---------")
foods = []
prices = []
total = 0

while True:
    food = input("Enter Food: (q To Exit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter Price Of {food}: $"))
        foods.append(food)
        prices.append(price)


print(f"You Chose {foods}")
print(f"With Prices Being {prices}")

for i in prices:
    total += i

print(f"Your Total is ${total}") 