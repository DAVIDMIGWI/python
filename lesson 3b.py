

a = 40
b = 50
c = 500

if a > b:
    print("A is greater than B")
    if a > c:
        print("A is also greater than C")
    else:
        print("A is not greater than C")
        if c > b:
            print("C is the largest")
        else:
            print("A is the largest")



else:
    if b > c:
        print("B is greater")
    else:
        print("its C")



