
# distance = x

x = float(input("Enter distance:_"))

if x > 0 and x < 100:
    print("The cost is 5.00")

elif x >= 100 and x <500:
    print(" The cost is 8.00")

elif x >= 500 and x <1000:
    print("The cost is 10.00")

else:
    print("The cost is 12.00")

