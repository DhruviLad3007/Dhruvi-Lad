# Bank Management System in Python

class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance.")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")


# Main Program
account = None

while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")
        acc_no = input("Enter account number: ")
        account = BankAccount(name, acc_no)
        print("✅ Account created successfully!")

    elif choice == "2":
        if account:
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)
        else:
            print("❗ Please create an account first.")

    elif choice == "3":
        if account:
            amt = int(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        else:
            print("❗ Please create an account first.")

    elif choice == "4":
        if account:
            account.check_balance()
        else:
            print("❗ Please create an account first.")

    elif choice == "5":
        print("👋 Thank you for using Bank Management System")
        break

    else:
        print("❌ Invalid choice. Try again.")
