# 4. Bank Account
# Create a BankAccount class with:
#     account_holder
#     balance
# Create methods:
#     deposit(amount)
#     withdraw(amount)
#     display_balance()
# Prevent the user from withdrawing more money than the current balance.

class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount        
        return f"PKR {amount} has been deposited to your account"
        
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient Balance. Please try another amount."
        else:
            self.balance -= amount
            return f"PKR {amount} has been withdrawn from your account."
        
    def display_balance(self):
        return f"You have PKR {self.balance} in your account {self.account_holder}"
    
    
if __name__ == "__main__":
    bank_account1 = BankAccount("Francis Parwez", 20000)
    print(bank_account1.display_balance())
    print(bank_account1.deposit(2000))
    print(bank_account1.withdraw(1500))
    print(bank_account1.withdraw(111500))
    print(bank_account1.display_balance())