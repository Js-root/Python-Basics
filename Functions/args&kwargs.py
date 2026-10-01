# *args = allows to pass multiple non-key arguments 
# **kwargs = allows to pass multiple keyword arguments 
# * is unpacking operator 

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(2,3,4))


def something(**kwargs):
    for i in kwargs.values():   
        print(i)

something(name = "somename",
          roll = 100,
          course = "LOOOL")

#Practice Questions:
def largest(*args):
    num = args[0]
    for i in args:
        if i>=num:
            num = i
    return num
print(largest(12,16,1,15,20,25,28))

#Practice Question 2:
def smallest(*args):
    num = args[0]
    for i in args:
        if num>=i:
            num = i
    return num

print(smallest(12,15,21,21,10,1,4,5))
