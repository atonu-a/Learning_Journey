print("== Welcome to Expense Tracker ==")

balance = 0

transaction = input("expense or income ? :")
if (transaction == "expense"):
    taka = int(input("How much ? : "))
    balance -= taka
    print(f"Your current balance is {balance} tk.")
elif(transaction == "income"):
    taka = int(input("How much ? : "))
    balance += taka
    print(f"Your current balance is {balance} tk.")
else:
    print("Please check your input and try again!")

print("== Thank Your For Using! ==")