#List Comprehension is a way to create lists in python 
#It is compact and easier to read 

#[Expression for Value in iterable if condition]  -->Syntax

#       doubles = []
#       for i in range(0,11):
#           doubles.append(i*2)   This Same code can be made short 

doubles = [i*2 for i in range(0,11)]
print(doubles)

#-------------------------------------------------------------
numbers = [1,2,-3,-4,5,-6,7,8]
pos_num = [num for num in numbers if num>=0]
even_num = [num for num in numbers if (num%2) == 0]
print(pos_num)
print(even_num)

#---------------------------------------------------------------
grades = [21,72,42,64,85,52,75,54]
passing_grades = [grade for grade in grades if grade>=60]
print(passing_grades)