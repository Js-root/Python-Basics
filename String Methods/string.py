name = input("Enter Your Name: ")

print(len(name))    #prints the length of name(includes space)
print(name.find("j"))   #gives index of j where it first came
print(name.rfind("j"))  #gives index of j where it last came
#if they dont find the letter then they return a -1 

print(name.capitalize()) #First Letter Is Capitalized
print(name.upper()) #Capitalizes all letters in a word 
print(name.lower()) #Lowercase all letters in a word
print(name.isdigit()) #Returns true if all letters are num
print(name.isalpha()) #Returns true if all letters are alphabet
print(name.count("J")) #Counts How many time j occured in word

print(name.replace("j", "s")) #Replaces j with s
print(name.replace(" ",""))
