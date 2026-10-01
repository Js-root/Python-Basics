# Switch Case also known as match case statements are alt. to using many elif statements and executes the code of certain values which matches the case.

def day(x):
    match x:
        case 1:
            return "Monday" #Returns Monday if input is 1
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:             #Default Case
            return "Nope Enter Between 1-7"

print(day(4))