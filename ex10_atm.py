balance = 10000
history = []

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        history.append("Deposited " + str(amount))
        print("Deposit successful")
        print("New Balance:", balance)

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance and balance - amount >= 500:
            balance = balance - amount
            history.append("Withdrew " + str(amount))
            print("Withdrawal successful")
            print("New Balance:", balance)
        else:
            print("Transaction not allowed")

    elif choice == "4":
        print("\nTransaction History:")
        if len(history) == 0:
            print("No transactions yet")
        else:
            for item in history:
                print(item)

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")