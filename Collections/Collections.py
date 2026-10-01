#Collections = Single variable used to store multiple values

#List = [] = Ordered, Changable and duplicates are allowed
#Set = {} = Unordered, Cannot Change and no duplicates
            #Set uses add,remove,pop function
#Tuple = () = Ordered, Cannot Change and duplicates allowed (fast)

fruits = ["Apple", "Banana", "Orange", "Mango"]

#print(len(fruits)) #Tells the length

#print("Apple" in fruits) #Returns true if found

fruits[0] = "grapes"

fruits.append("Pineapple") #Adds pineapple to end of list

fruits.remove("grapes") #Removes the element from list

fruits.insert(0,"Apple") #Insert lets you add to any index

fruits.sort() #Sorts Out The List
 
fruits.reverse() #Reverses the list 

#fruits.clear() - clears whole list

print(fruits.index("Banana")) #Tells us index of banana
print(fruits.count("Banana")) #Tells us how many banana in list 

for i in fruits:
    print(i)