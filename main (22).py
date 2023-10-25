class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds. Cannot withdraw specified amount.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: {self.__account_balance}")


# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe")

# Test deposit functionality
account.deposit(500)
account.display_balance()

# Test withdrawal functionality
account.withdraw(200)
account.display_balance()