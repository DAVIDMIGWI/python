

# create a payroll
# you will find gross and net pay
# variables needed basic salary, house allowance, transport allows
# deductions nssf, nhif tax
# the function is called payroll
#must use parameters



def payroll():

    salary = float(input("Enter salary:"))
    house_allowance = salary * 0.18
    print("house allowance", house_allowance )
    transport_alowance = salary * 0.2
    gross = salary + house_allowance + transport_alowance

    # deductions
    nssf = basic * 0.11
    nhif = basic * 0.14
    tax = gross * 0.115

    HRA = basic * 0.1;
    DA = basic * 0.05;
    PF = basic * 0.12;
    
