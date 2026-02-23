print("=== BILL SPLITTER ===")

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax = float(input("Enter tax percentage: "))
tip = float(input("Enter tip percentage: "))

tax_amount = total_bill * tax / 100
after_tax = total_bill + tax_amount

tip_amount = after_tax * tip / 100
total = after_tax + tip_amount

per_person = total / people

print("\nTotal Bill:", total)
print("Amount per person:", per_person)