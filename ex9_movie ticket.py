age = int(input("Enter your age: "))
day = input("Enter day of the week: ").lower()
tickets = int(input("Enter number of tickets: "))

if age < 3:
    ticket_price = 0
elif 3 <= age <= 12:
    ticket_price = 150
elif 13 <= age <= 59:
    ticket_price = 300
else:
    ticket_price = 200
base_price = ticket_price * tickets
if day in ["friday", "saturday", "sunday"]:
    discount = base_price * 0.20
else:
    discount = 0
price_after_discount = base_price - discount
total_amount = price_after_discount
print("\n----- BILL SUMMARY -----")
print("Base Price:", base_price)
print("Discount:", discount)
print("Price After Discount:", price_after_discount)
print("Total Amount:", total_amount)