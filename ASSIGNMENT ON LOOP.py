

number = float(input("Enter the number for multiplication table: "))

print("The Multiplication Table of: ", number)
for count in range(1, 13):
    print(number, 'x', count, '=', number * count)
