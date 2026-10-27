# 16. Class Variable — Employee Count
# Create an Employee class.
#     Every time an employee object is created, increase:
# employee_count
# Example:
#     e1 = Employee("Ali")
#     e2 = Employee("Ahmed")
#     e3 = Employee("Sara")
# Output:
#     Total employees: 3
# Then create a class method:
#     get_employee_count()
# that returns the number of employees.
# Practice: class variables + @classmethod 

class Employee:
    employee_count = 0
    
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
        
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
        
if __name__ == '__main__':
    e1 = Employee("Ali")
    e2 = Employee("Ahmed")
    e3 = Employee("Sara")

    print(f"Total employees: {Employee.get_employee_count()}")