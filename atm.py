account = {
    "pin": 1234,
    "balance": 50000
}

def check_balance():
    print("Your balance is:", account["balance"])



def deposit():
    amount = int(input("Enter deposit amount: "))

    if amount > 0:
        account["balance"] = account["balance"] + amount
        print("Current balance:", account["balance"])
    else:
        print("Enter a valid amount!")



def withdraw():
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount!")
    elif amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Remaining balance:", account["balance"])
    else:
        print("Insufficient balance!")



pin = int(input("Enter your ATM PIN: "))

if pin == account["pin"]:
    print("\nLogin successful!")

    
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid! Try again.")

else:
    print("Invalid pin")
