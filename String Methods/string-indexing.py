#Indexing means accesing elements of a sequence using []
# [start:end:step] start = it is inclusive
#                  end = it is exclusive
# This means if start = 0 and end = 4 then we would get elements from 0-3 index

number = "123456789"
print(number[0]) #We Get 1
print(number[0:4]) #We Get 1234
print(number[4:8]) #We Get 5678
print(number[4:]) #Gives 56789 (all till end)
print(number[-1]) #Gives 9 (if we set it to -2 then it gives 8)
print(number[::2]) #We use step here this will print all numbers but with gap of 2 between them (1,3,5,7,9)

#What if we wanna reverse the whole string??
reverse = number[::-1]
print(reverse) #We get reverse of the string 