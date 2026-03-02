def deposit_logic():
    user_input = input("Enter 'deposit' to make a deposit: ")
    if user_input == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        balance = 0
        if amount > 0:
            balance += amount
            print(f"Deposit successful! Your new balance is: {balance}")
        else:
            print("Invalid amount. Please enter a positive number.")


deposit_logic()