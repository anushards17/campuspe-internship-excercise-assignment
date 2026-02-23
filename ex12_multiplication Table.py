number = int(input("Enter number: "))
end_range = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)
print("-" * 25)

for i in range(1, end_range + 1):
    result = number * i
    print(f"{number:>2} x {i:>2} = {result:>3}")

print("-" * 25)