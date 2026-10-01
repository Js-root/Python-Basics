#2D list is nthing but collection of lists

fruits =   ["Apple", "Mango", "Banana"]
cars =     ["Lambo", "Ferrari", "Byd"]
hardware = ["Keyboard", "Monitor", "Mic"]

random = [fruits, cars, hardware]

print(random[1][0])

for i in random:
    for x in i:
        print(x , end=" ")
    print()
