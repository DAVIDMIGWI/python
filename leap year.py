
# leap year
# if year not div by 4 - not leap year
#if a year divisible by 4, 100, 400 its a leap year.

year = int(input("enter year: "))
if year%4 != 0:
    print("not a leap year")

elif year%4 == 0 and year%100 !=0:
    print("its a leap year")

elif year%4 ==0 and year%100 ==0 and year%400 ==0:
    print("its a leap year")

else:
    print("its not a leap year")