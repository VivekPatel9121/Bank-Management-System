# bank_management.py

accounts = []


def create_account():
    print("\n===== Create New Account =====")
    account_number = input("Enter Account Number: ").strip()
    name = input("Enter Account Holder Name: ").strip()
    balance_input = input("Enter Initial Balance: ").strip()

    if not balance_input.replace('.', '', 1).isdigit():
        print("Invalid balance. Please enter a numeric value.\n")
        return

    balance = float(balance_input)

    for account in accounts:
        if account["account_number"] == account_number:
            print("Account number already exists.\n")
            return

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }

    accounts.append(account)
    print("Account created successfully.\n")


def view_accounts():
    print("\n===== View All Accounts =====")
    if not accounts:
        print("No accounts found.\n")
        return

    for account in accounts:
        print(f"Account Number: {account['account_number']}")
        print(f"Account Holder Name: {account['name']}")
        print(f"Balance: ₹{account['balance']:.2f}")
        print("-" * 30)
    print()


def search_account():
    print("\n===== Search Account =====")
    account_number = input("Enter Account Number: ").strip()

    for account in accounts:
        if account["account_number"] == account_number:
            print("Account found:")
            print(f"Account Number: {account['account_number']}")
            print(f"Account Holder Name: {account['name']}")
            print(f"Balance: ₹{account['balance']:.2f}\n")
            return

    print("Account not found.\n")


def deposit_money():
    print("\n===== Deposit Money =====")
    account_number = input("Enter Account Number: ").strip()
    amount_input = input("Enter amount to deposit: ").strip()

    if not amount_input.replace('.', '', 1).isdigit():
        print("Invalid amount.\n")
        return

    amount = float(amount_input)

    if amount <= 0:
        print("Amount must be greater than 0.\n")
        return

    for account in accounts:
        if account["account_number"] == account_number:
            account["balance"] += amount
            print(f"Deposit successful. New balance: ₹{account['balance']:.2f}\n")
            return

    print("Account not found.\n")


def withdraw_money():
    print("\n===== Withdraw Money =====")
    account_number = input("Enter Account Number: ").strip()
    amount_input = input("Enter amount to withdraw: ").strip()

    if not amount_input.replace('.', '', 1).isdigit():
        print("Invalid amount.\n")
        return

    amount = float(amount_input)

    if amount <= 0:
        print("Amount must be greater than 0.\n")
        return

    for account in accounts:
        if account["account_number"] == account_number:
            if amount > account["balance"]:
                print("Insufficient balance.\n")
            else:
                account["balance"] -= amount
                print(f"Withdrawal successful. Remaining balance: ₹{account['balance']:.2f}\n")
            return

    print("Account not found.\n")


def delete_account():
    print("\n===== Delete Account =====")
    account_number = input("Enter Account Number to delete: ").strip()

    for account in accounts:
        if account["account_number"] == account_number:
            accounts.remove(account)
            print("Account deleted successfully.\n")
            return

    print("Account not found.\n")


def menu():
    while True:
        print("===== Bank Management System =====")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            search_account()
        elif choice == "4":
            deposit_money()
        elif choice == "5":
            withdraw_money()
        elif choice == "6":
            delete_account()
        elif choice == "7":
            print("Thank you for using Bank Management System.")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()