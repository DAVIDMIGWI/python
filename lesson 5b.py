# Lists vs Tuples
# both are used to store many values in a single variable.

# LIST EXAMPLE
# uses () to enclose many values
age = [40, 50, 37, 48, 47, 80, 80.3, 77]
print(age)

# a list of strings
towns = ["Nairobi", "KISUMU", "Eldoret", "Mombasa", "Nakuru"]
print(towns)

# lets do slicing, count from zero
print(age[0])  # print the first item
print(age[0:10])  # print from zero to 10
print(age[5:10])  # print from 5 to 10
print(age[5:])  # assumes 5 and above
print(age[:])  # all of them

# for towns
print(towns[:3])  # upto the 3rd town

# a list is mutable/ its flexible
# list are flexible
towns.append("kajiado")
towns.remove("KISUMU")
towns.insert(2,"Thika")
print(towns)
