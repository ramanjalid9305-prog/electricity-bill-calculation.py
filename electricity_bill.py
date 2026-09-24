def calculate_bill(units):
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 300:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.00)

    return bill


print("===== Electricity Bill Calculator =====")

try:
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Units cannot be negative.")
    else:
        bill = calculate_bill(units)
        print(f"Electricity Units : {units}")
        print(f"Total Bill       : ₹{bill:.2f}")

except ValueError:
    print("Please enter a valid number.")
