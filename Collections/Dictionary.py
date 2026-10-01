#Dictionary  = A collection of {key:value} pair
#              Ordered, Can Change and No Duplicates

game = {"Title":"Minecraft",
        "Developer": "Mojang",
        "Year": "2011",
        "Rating": "9.5"}

print(game.get("Title"))

if game.get("Titlee"): #Returns True if found
    print("Game Exists")

game.update({"Good?":"Yesssssss"}) #Adds to the dictionary
game.update({"Players?":"Yeahhhhh"})
game.update({"Year":"2007"}) #Updates The Value of "Year" Key
game.pop("Rating") #Removes "Rating" key and value
game.popitem() #Removes Latest Key Value Pair
#game.clear() - Clears Whole Dictionary

keys = game.keys() #Gets All The Keys Present
print(keys)

values = game.values() #Gets All The Values Present
print(values)

items = game.items() #Gets All Key-Value Pairs
print(items)
for i,x in items:
    print(f"{i} --> {x}")
