
# create a payroll
# you will find gross and net pay
# variables needed basic salary, house allowance, transport allows
# deductions nssf, nhif tax
# the function is called payroll
#must use parameters


def payroll(gross,):
    #gross = 27000
    nssf = gross * 0.12
    nhif = gross * 0.06
    house  = gross * 0.5
    transport = gross * 0.44
    tax = (house + transport + gross) * 0.2

    deductions = nssf + nhif + tax
    print("Total Deductions", deductions)
    print("NSSF", nssf)
    print("NHIF", nhif)
    print("TAX", tax)
    print("House allowance", house)
    print("Transport allowance", transport)

    Salary = house + transport + gross - deductions
    print("your basic salary is ",Salary, "KSH")


