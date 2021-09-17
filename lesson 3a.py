
# nested statements - this are if statement inside another

x = 6

if x > 10:
    print("its greater than 10")

else:
    print(" its less then 10")
    if x > 20:
        print("its still more than 20")
    else:
        print("its less than 20")
        if x < 10:
            print("invalid")
        else:
            print("valid")
            

