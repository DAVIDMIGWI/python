# creating files, reading , writing, closing files in python
# w mode create the file if it doesn't exits

file = open("countries.txt", mode="w")
with open("countries.txt", mode="w") as file:
    file.write("kenya\n")
    file.write("uganada\n")
    file.write("tanzania\n")
    file.write("countries in EA\n")
    file.write("italy")
    print("file writing done")

# read the file
# r mode cannot create a file only w can
# an exception is a process or a task that stops the program at a point.
# exceptions are raised if there is something unusual
# i.e no data base, file does not exist, image too big a wrong calculation, wrong math

try:
    file = open("countries.txt", mode="r")  # open the file if its there
    print(file.read())
except:
    print("file not found")  # catches the exception just in case the files are not available
finally:
    print("Do this either error or Not")  # this task runs either error or not
    file.close()

print("======================================")

# method 2 use a loop
list = []  # empty list
file = open("countries.txt", mode="r")
for line in file:
    print(line, end=" ")
    list.append(line) # append each line to a list

    print("file not found")

    print(list)
