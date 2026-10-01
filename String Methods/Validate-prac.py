#Valid User Input Exercise
# 1) Username No more than 12 characters
# 2) username must not have space
# 3) username must not have digits (numbers)

print("-----------Welcome To The Forms-----------")
name = input("Enter Username: ")
name = name.replace(" ","")

if len(name) >= 12:
    print("Username Cant Be More Than 12 Characters.")

elif not name.isalpha():
    print("Username Cannot Have Numbers")

else:
    print(f"Your Username Is: {name}")