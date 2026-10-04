# 11. Employee Inheritance 👨‍💼
# Create a base class:
#     Employee
# with:
#     name
#     salary
# Create two child classes:
#     Manager
#     Developer
# Add a method:
#     calculate_bonus()
# Rules:
#     Manager → 20% of salary
#     Developer → 10% of salary
# Practice: inheritance and method overriding


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary        
        
class Manager(Employee):    
    def calculate_bonus(self):
        return self.salary + (self.salary * 0.2)
    
class Developer(Employee):    
    def calculate_bonus(self):
        return self.salary + (self.salary * 0.1)
    
if __name__ == '__main__':
    manager = Manager("Alice", 75000)
    developer = Developer("Faizan", 35000)
    
    print(f"{manager.name} Receives The Salary Of {manager.calculate_bonus():.2f} Each Month After 20% Bonus")
    print(f"{developer.name} Receives The Salary Of {developer.calculate_bonus():.2f} Each Month After 10% Bonus")
        
    
        
    