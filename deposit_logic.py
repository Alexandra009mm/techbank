def deposit_logic(balance):
    
        amount = float(input("Enter the amount to deposit: "))
        
        if amount > 0:
            balance += amount
            print(f"Deposit successful! Your new balance is: {balance}")
        else:
            print("Invalid amount. Please enter a positive number.")

    