# case when wa have one variable

points = float(input("Enter your points:-"))

if points < 100:
     print("You don't qualify")

elif points >= 100 and points <200:
    print("You qualify for 50 ksh Airtime")

elif points >= 200 and points < 500:
    print("you qualify for 500mb free data")

elif points >= 500 and points < 1000:
    print("you qualify for a smart phone")

else:
    print("you will a Bike") # 1000