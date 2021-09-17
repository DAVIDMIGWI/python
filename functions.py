# function is a piece of code performing specific task.
# functions don't run unless they are called/trigger.
# functions break a bigger code to small pieces.
# using functions makes code easy to manage and understand
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result


def addition():
    a = 40
    b = 56
    answer = a + b
    print("The answer is", answer)


def subtract():
    a = 88
    b = 72
    answer = a - b
    print("The difference is", answer)


def bmi(weight,height):
    # find body mass index
    # formula weight/height/squared
    # declare

    print("Body mass index")
    print("formula is weight/height/squared ")
    #weight = 56
    #height = 1.5
    answer = (weight / (height * height))
    print("BMI is", answer, " kg/m2")




def simple_interest(principle, time):
    # principle = 5200
    RATE = 1.5
    # time=4
    interest = principle * RATE / 100 * time
    print("you will pay", interest)


# create a function area circle

# formula is pi R squred
def area_circle():
    PI = 3.14
    radius = 15
    area = PI * radius * radius
    print("The area of the cirle is", area, "M2")

