#Well its just loop inside loop

rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))
symbol = input("Enter A Symbol To Use: ")

for i in range(rows):
    
    for x in range(columns):
        print(symbol, end="")

    print()