# 13. Private Bank Account 🔐
# Improve the previous BankAccount class.
# Make the balance private:
#     __balance
# Create methods:
#     deposit()
#     withdraw()
#     get_balance()
# The user should not be able to directly modify the balance through the normal public
# interface.
# Practice: encapsulation and private attributes

class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"PKR {amount} has been deposited to your account"

    def withdraw(self, amount):
        if self.__balance < amount:
            return "Insufficient Balance. Please try another amount."
        else:
            self.__balance -= amount
            return f"PKR {amount} has been withdrawn from your account."
        
    def get_balance(self):
        return self.__balance
    
    
if __name__ == "__main__":
    bank_account1 = BankAccount("Francis Parwez", 20000)
    
    print(f"Initial Balance: PKR {bank_account1.get_balance()}")
    print(bank_account1.deposit(2000))
    print(bank_account1.withdraw(1500))
    print(bank_account1.withdraw(111500))
    print(f"Final Balance: PKR {bank_account1.get_balance()}")