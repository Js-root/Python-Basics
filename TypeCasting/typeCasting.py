#TypeCasting is a Process Of Converting A Variable From One Data Type to Another

# int(), Str(), float(), bool()
name = "Guest"
age = 28
gpa = 9.0
is_Student = True


print(type(age)) #Shows Datatype of Variable

age = str(age) #Age Is Now A String
gpa = int(gpa) #Gpa Is Now Int 
nameNull = bool(name)

stringNumber = name+age

print(f"{nameNull}") #Checks If name is null or not 
print(f"{age}")
print(f"{gpa}")
print(f"{stringNumber}") #Adds Both The Strings
