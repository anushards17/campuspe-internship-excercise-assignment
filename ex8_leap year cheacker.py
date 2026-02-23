year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
    print("Reason: It follows the leap year rule.")
else:
    print(year, "is NOT a Leap Year.")
    print("Reason: It does not satisfy the leap year conditions.")