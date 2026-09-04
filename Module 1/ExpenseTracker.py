print("== Welcome to Expense Tracker ==")

balance = 0


while True:
    transaction = input("Enter e for expense, i for income and b for balance :")
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
    else:
        print("Please check your input and try again!")

    print("== Thank Your For Using! ==")