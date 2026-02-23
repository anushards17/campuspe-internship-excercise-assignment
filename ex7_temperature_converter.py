# ex7_temperature_converter.py

print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)

elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius:", c)

elif choice == 3:
    c = float(input("Enter Celsius: "))
    k = c + 273.15
    print("Kelvin:", k)

elif choice == 4:
    k = float(input("Enter Kelvin: "))
    c = k - 273.15
    print("Celsius:", c)

elif choice == 5:
    f = float(input("Enter Fahrenheit: "))
    k = (f - 32) * 5/9 + 273.15
    print("Kelvin:", k)

elif choice == 6:
    k = float(input("Enter Kelvin: "))
    f = (k - 273.15) * 9/5 + 32
    print("Fahrenheit:", f)

else:
    print("Invalid choice")