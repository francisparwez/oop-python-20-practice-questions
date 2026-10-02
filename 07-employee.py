# 7. Employee Class
# Create an Employee class with:
#     name
#     salary
# Create a method:
#     give_raise(amount)
# that increases the employee's salary.
# Example:
#     Salary before: 50000
#     Salary after: 60000

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
        else:
            print("Invalid Amount. Enter a non-zero/non-negative number")
    
    
if __name__ == "__main__":
    employee1 = Employee('Francis', 50000)
    print(f"Salary before: {employee1.salary}")
    employee1.give_raise(10000)
    print(f"Salary after: {employee1.salary}")