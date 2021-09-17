
# dictionaries
# dictionary is used to store an object details
# dictionary stores data using key - value approach

vehicle={
        "make":"toyota",
        "model":"fielder",
        "year" : 2009,
        "cost":5872990,
        "color":"silver",
        "reg":"KBN88R"
  }
print(vehicle)
print(vehicle["reg"])
print(vehicle["year"])

vehicle["color"]="blue"  #update
vehicle["cost"]= 790000  #update
vehicle["doors"]=5 #adding
#print the dictionary
print("uptadeted", vehicle)

# deleting
del vehicle["model"]
print("model deleted", vehicle)

# 1. create a list/tuple of points, there at least 10 items
# find the sum of all the points

# 2. create a list/tuple of counties at least 8 conties
#loop through counties, stop the loop eg. embu county



