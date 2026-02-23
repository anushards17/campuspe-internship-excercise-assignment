
print("Choose Pattern:")
print("1. Increasing Numbers")
print("2. Repeating Numbers")
print("3. Reverse Numbers")
print("4. Pyramid Numbers")
print("5. Increasing Stars")
print("6. Decreasing Stars")
print("7. Number Square ")

choice = int(input("Enter choice: "))
n = int(input("Enter height/size: "))
if choice == 1:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
elif choice == 2:
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()
elif choice == 3:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
elif choice == 4:
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(j, end="")
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()
elif choice == 5:
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()
elif choice == 6:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
elif choice == 7:
    for i in range(n):
        for j in range(1, n+1):
            print(j, end=" ")
        print()

else:
    print("Invalid choice")