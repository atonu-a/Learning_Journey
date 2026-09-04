print("== Welcome to Expense Tracker ==")

balance = 0


while True:
    transaction = input("Enter e for expense, i for income, b for balance and exit for exit : ")
    if (balance<=0 and transaction == "e"):
        print("You don't have sufficient balance to expense! ")
    else:       
        if (transaction == "e"):
            taka = int(input("How much ? : "))
            balance -= taka
            print(f"Your current balance is {balance} tk.")
        elif(transaction == "i"):
            taka = int(input("How much ? : "))
            balance += taka
            print(f"Your current balance is {balance} tk.")
        elif(transaction == "b"):
            print(f"Your current balance is {balance} tk.")
        elif(transaction == "exit"):
            break
        else:
            print("Please check your input and try again!")

print("== Thank Your For Using! ==")