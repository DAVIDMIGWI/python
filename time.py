
# create a program to find the current date and time any imports

def time():
    import datetime
    from datetime import date
    now = datetime.datetime.now()
    print("current date and time is-")
    print(now.strftime("%y-%m-%d %H-%M-%S"))

def random():
    import random
    x = random.randint(0, 101)
    print( "The random number is", x)

def codetest():
    import random

    mylist = []

    for i in range(50,400):
        x = random.randint(1500, 40000)
        mylist.append(x)

    print(mylist)


time()
random()