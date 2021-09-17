

units = float(input("Enter your units:-"))
if units < 50:
    total = units * 0.5
    print("Kindly pay",total,"Rs")
    print("Inc. surcharge", total + 10)

elif units > 50 and units <=150:
    pay1 = 50 * 0.5
    pay2 = units - 50 * 1
    total = pay1 + pay2
    print("pay",total)
    print("Inc. surcharge", total + 10)

elif units > 150 and units < 250:
    pay1 = 50 * 0.5
    pay2 = 100 * 1
    pay3 = units - 150 * 1.2
    total = pay3 +pay1 +pay2
    print("Kindly pay", total, "Rs")
    print("Inc. surcharge", total + 10)

else:
    pay1 = 50 * 0.5
    pay2 = 100 * 1
    pay3 = 100 * 1.2
    pay4 = units - 250 * 1.5
    total = pay3 + pay1 + pay2 + pay4
    print("Kindly pay", total, "Rs")
    print("Inc. surcharge", total + 10)
