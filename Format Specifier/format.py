#Format Specifiers are used to make values look as whatever flag was entered

# {value:flags}

price1 = 3.145125
price2 = -123456
price3 = 12384023

print(f"{price3:,}") #  (,) adds , to thousands (run code)
print(f"{price1:+}") #  + adds + to +ve num and - to -ve
print(f"{price2:10}")#  makes digit 10 digits long 
print(f"{price3:010}")# makes digit 10 digits long and add 0 in front
print(f"{price1:.2f}")# This means that make only 2 decimals visible

#we can use them together aswell
print(f"{price1:+,.2f}")