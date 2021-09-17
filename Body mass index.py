# find body mass index
# formula weight/height/squared
 # declare

print("Body mass index")
print("formula is weight/height/squared ")
weight = 56
height = 1.5
print("Weight = 58 KGS")
print("Height = 1.5 Meters")
answer = (weight/(height*height))
print("BMI is",answer," kg/m2")

if answer < 18.5:
    print("underweight")

elif answer >= 18.5 and answer <22.9:
    print("Normal")

elif answer >= 23 and answer <24.9:
    print("overweight")

elif answer >= 25 and answer <29.9:
    print("pre-obese")

elif answer >= 30 and answer <34.9:
    print("obese class")

elif answer >= 35 and answer <39.9:
    print("obese class II")

else:
    print("obese class III")
