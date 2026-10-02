# 20 Python OOP Practice Questions

A progressive set of **20 Python Object-Oriented Programming (OOP) practice problems**, divided into:

- 🟢 **10 Easy**
- 🟡 **10 Intermediate**

The exercises progress from basic classes and instance methods to inheritance, encapsulation, class/static methods, operator overloading, polymorphism, and a small employee management system.

---

## 📚 Practice Questions

### 🟢 Easy Level

| #   | Problem           | Main Concepts                                     | Status         |
| --- | ----------------- | ------------------------------------------------- | -------------- |
| 1   | Person Class      | `__init__`, instance attributes, instance methods | ✅ Completed   |
| 2   | Student Class     | `__init__`, instance attributes, methods          | ✅ Completed   |
| 3   | Rectangle Class   | Methods, calculations, instance attributes        | ✅ Completed   |
| 4   | Bank Account      | Methods, validation, state management             | ✅ Completed   |
| 5   | Car Class         | Instance attributes, methods                      | ✅ Completed   |
| 6   | Circle Class      | Methods, calculations                             | ✅ Completed   |
| 7   | Employee Class    | Methods, modifying object state                   | ✅ Completed   |
| 8   | Book Class        | Methods, percentage calculations                  | ⬜ Not Started |
| 9   | Counter Class     | Instance state, increment/decrement/reset         | ⬜ Not Started |
| 10  | Temperature Class | Methods, unit conversion                          | ⬜ Not Started |

### 🟡 Intermediate Level

| #   | Problem                    | Main Concepts                                             | Status         |
| --- | -------------------------- | --------------------------------------------------------- | -------------- |
| 11  | Employee Inheritance       | Inheritance, method overriding                            | ⬜ Not Started |
| 12  | Animal Polymorphism        | Inheritance, polymorphism, method overriding              | ⬜ Not Started |
| 13  | Private Bank Account       | Encapsulation, private attributes                         | ⬜ Not Started |
| 14  | Shopping Cart              | Multiple classes, lists of objects, object interaction    | ⬜ Not Started |
| 15  | Library Management System  | Multiple classes, object state, object interaction        | ⬜ Not Started |
| 16  | Employee Count             | Class variables, `@classmethod`                           | ⬜ Not Started |
| 17  | Email Validation           | `@staticmethod`, validation                               | ⬜ Not Started |
| 18  | Vector                     | Operator overloading, `__add__()`, `__str__()`            | ⬜ Not Started |
| 19  | E-Commerce Product System  | Inheritance, overriding, polymorphism                     | ⬜ Not Started |
| 20  | Employee Management System | OOP integration, inheritance, encapsulation, polymorphism | ⬜ Not Started |

---

# 🟢 Easy Level

## 1. Person Class ✅

### Problem

Create a `Person` class with:

- `name`
- `age`

Add a method `introduce()` that prints:

```text
My name is Ali and I am 25 years old.
```

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- `if __name__ == "__main__":`

### Solution

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


if __name__ == "__main__":
    person1 = Person("Francis", 31)
    person1.introduce()
```

### Output

```text
My name is Francis and I am 31 years old
```

### What I Learned

- `self` refers to the current object.
- `__init__()` initializes the object's attributes when an object is created.
- Instance methods need `self` as their first parameter.
- `if __name__ == "__main__":` allows code to run when the file is executed directly.

---

## 2. Student Class ✅

### Problem

Create a `Student` class with:

- `name`
- `student_id`
- `grade`

Add a method `display_info()` that displays all three attributes.

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- `if __name__ == "__main__":`

### Solution

```python
class Student:

    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}\nStudent ID: {self.student_id}\nGrade: {self.grade}")


if __name__ == "__main__":
    student1 = Student('Francis', '38332', 'F')
    student1.display_info()
```

### Output

```text
Student Name: Francis
Student ID: 38332
Grade: F
```

### What I Learned

- A class can contain multiple instance attributes.
- `self` is used to access attributes belonging to the current object.
- `display_info()` can access and display object data through `self`.
- Objects are created by calling the class with the required arguments.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

---

## 3. Rectangle Class ✅

### Problem

Create a `Rectangle` class with:

- `length`
- `width`

Create methods:

- `area()`
- `perimeter()`

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- Returning calculated values
- `if __name__ == "__main__":`

### Solution

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    print(rectangle.area())
    print(rectangle.perimeter())
```

### Output

```text
50
30
```

### What I Learned

- A class can store multiple related attributes such as `length` and `width`.
- Instance methods can perform calculations using the object's attributes.
- `return` sends the calculated result back to the caller.
- The area of a rectangle is calculated using `length × width`.
- The perimeter is calculated using `2 × (length + width)`.
- An object can be created with specific values and its methods can then be called to perform calculations.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

**Status:** ✅ Completed

---

## 4. Bank Account ✅

### Problem

Create a `BankAccount` class with:

- `account_holder`
- `balance`

Create methods:

- `deposit(amount)`
- `withdraw(amount)`
- `display_balance()`

Prevent the user from withdrawing more money than the current balance.

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- Modifying object state
- Conditional logic and validation
- Returning values from methods
- `if __name__ == "__main__":`

### Solution

```python
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
```

### Output

```text
You have PKR 20000 in your account Francis Parwez
PKR 2000 has been deposited to your account
PKR 1500 has been withdrawn from your account.
Insufficient Balance. Please try another amount.
You have PKR 20500 in your account Francis Parwez
```

### What I Learned

- A class can store account information using instance attributes.
- Methods can modify the object's state, such as increasing or decreasing the balance.
- `deposit()` increases the account balance.
- `withdraw()` checks the current balance before allowing a withdrawal.
- Conditional logic can be used to prevent invalid operations.
- `return` allows methods to send messages back to the caller.
- The balance remains unchanged when a withdrawal is greater than the available balance.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

**Status:** ✅ Completed

---

## 5. Car Class ✅

### Problem

Create a `Car` class with:

- `brand`
- `model`
- `year`

Create a method:

```python
display_info()
```

that displays the car information in the format:

```text
Toyota Corolla (2022)
```

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- Returning formatted strings
- `if __name__ == "__main__":`

### Solution

```python
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2022)
    print(car1.display_info())
```

### Output

```text
Toyota Corolla (2022)
```

### What I Learned

- A class can store related information such as a car's brand, model, and year.
- `__init__()` initializes the attributes when a `Car` object is created.
- `self` is used to access attributes belonging to the current object.
- `display_info()` can combine multiple attributes into one formatted string.
- `return` sends the formatted result back to the caller, where it can be printed.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

**Status:** ✅ Completed

---

## 6. Circle Class ✅

### Problem

Create a `Circle` class with:

- `radius`

Create methods:

- `area()`
- `circumference()`

Use:

```text
π = 3.14159
```

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- Class attributes
- `self`
- Instance methods
- Mathematical calculations
- Returning calculated values
- `if __name__ == "__main__":`

### Solution

```python
class Circle:

    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.pi * self.radius


if __name__ == "__main__":
    circle1 = Circle(20)

    print(circle1.area())
    print(circle1.circumference())
```

### Output

```text
1256.636
125.6636
```

### What I Learned

- A class can contain a class attribute such as `pi` that is shared by instances.
- `self.radius` stores the radius for each individual `Circle` object.
- `area()` calculates the area using the circle's radius.
- `circumference()` calculates the circumference using the circle's radius.
- `Circle.pi` explicitly accesses the class attribute.
- `return` sends the calculated result back to the caller.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

**Status:** ✅ Completed

---

## 7. Employee Class ✅

### Problem

Create an `Employee` class with:

- `name`
- `salary`

Create:

```python
give_raise(amount)
```

to increase the employee's salary.

Example:

```text
Salary before: 50000
Salary after: 60000
```

### Concepts Practiced

- Creating a class
- `__init__()`
- Instance attributes
- `self`
- Instance methods
- Modifying object state
- Conditional logic and validation
- `if __name__ == "__main__":`

### Solution

```python
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
    employee1 = Employee("Francis", 50000)

    print(f"Salary before: {employee1.salary}")
    employee1.give_raise(10000)
    print(f"Salary after: {employee1.salary}")
```

### Output

```text
Salary before: 50000
Salary after: 60000
```

### What I Learned

- An object can store employee information using instance attributes.
- Methods can modify an object's state by changing its attributes.
- `give_raise()` increases the employee's salary by the given amount.
- Conditional logic can be used to reject invalid raise amounts.
- `self.salary += amount` updates the existing salary stored in the object.
- `if __name__ == "__main__":` keeps the test code from running when the file is imported.

**Status:** ✅ Completed

---

## 8. Book Class

Create a `Book` class with:

- `title`
- `author`
- `price`

Create:

```python
apply_discount(percent)
```

to reduce the book price.

Example:

```text
Original price: 1000
Discount: 20%
New price: 800
```

**Status:** ⬜ Not Started

---

## 9. Counter Class

Create a `Counter` class with:

```python
count = 0
```

Create methods:

- `increment()`
- `decrement()`
- `reset()`
- `display()`

Example:

```text
0 → 1 → 2 → 1 → 0
```

**Status:** ⬜ Not Started

---

## 10. Temperature Class

Create a `Temperature` class with:

- `celsius`

Create methods:

- `to_fahrenheit()`
- `to_kelvin()`

Use the appropriate conversion formulas.

**Status:** ⬜ Not Started

---

# 🟡 Intermediate Level

## 11. Employee Inheritance

Create a base class:

```python
Employee
```

with:

- `name`
- `salary`

Create child classes:

```python
Manager
Developer
```

Add:

```python
calculate_bonus()
```

Rules:

- Manager → 20% of salary
- Developer → 10% of salary

**Concepts:** inheritance and method overriding.

**Status:** ⬜ Not Started

---

## 12. Animal Polymorphism

Create a base class:

```python
Animal
```

with:

```python
speak()
```

Create:

- `Dog`
- `Cat`
- `Cow`

Each class should override `speak()`.

Expected:

```text
Dog: Woof
Cat: Meow
Cow: Moo
```

Then create a list containing different animals and call `speak()` using a loop.

**Concept:** polymorphism.

**Status:** ⬜ Not Started

---

## 13. Private Bank Account

Improve the `BankAccount` class.

Make the balance private:

```python
__balance
```

Create:

- `deposit()`
- `withdraw()`
- `get_balance()`

The user should not be able to directly modify the balance through the normal public interface.

**Concepts:** encapsulation and private attributes.

**Status:** ⬜ Not Started

---

## 14. Shopping Cart

Create:

```python
Product
ShoppingCart
```

### Product

Contains:

- `name`
- `price`
- `quantity`

### ShoppingCart

Create:

- `add_product()`
- `remove_product()`
- `calculate_total()`
- `display_cart()`

Example:

```text
Laptop × 1 = 100000
Mouse × 2 = 3000

Total = 103000
```

**Status:** ⬜ Not Started

---

## 15. Library Management System

Create:

```python
Book
Library
```

### Book

Contains:

- `title`
- `author`
- `isbn`
- `available`

### Library

Create:

- `add_book()`
- `remove_book()`
- `borrow_book()`
- `return_book()`
- `display_books()`

A user should not be able to borrow a book that is already borrowed.

**Status:** ⬜ Not Started

---

## 16. Class Variable — Employee Count

Create an `Employee` class.

Every time an employee object is created, increase:

```python
employee_count
```

Example:

```python
e1 = Employee("Ali")
e2 = Employee("Ahmed")
e3 = Employee("Sara")
```

Output:

```text
Total employees: 3
```

Create a class method:

```python
get_employee_count()
```

that returns the number of employees.

**Concepts:** class variables and `@classmethod`.

**Status:** ⬜ Not Started

---

## 17. Static Method — Validate Email

Create a `User` class with:

- `name`
- `email`

Create:

```python
is_valid_email(email)
```

as a static method.

It should return `True` if the email contains:

```text
@
.
```

Otherwise return `False`.

Example:

```python
User.is_valid_email("ali@gmail.com")
```

Output:

```text
True
```

**Concept:** `@staticmethod`.

**Status:** ⬜ Not Started

---

## 18. Operator Overloading

Create a `Vector` class with:

- `x`
- `y`

Create:

```python
v1 = Vector(2, 3)
v2 = Vector(4, 5)
```

Allow:

```python
v3 = v1 + v2
```

to produce:

```text
Vector(6, 8)
```

Implement:

```python
__add__()
```

Also implement:

```python
__str__()
```

so:

```python
print(v3)
```

outputs:

```text
(6, 8)
```

**Status:** ⬜ Not Started

---

## 19. E-Commerce Product System

Create a base class:

```python
Product
```

with:

- `name`
- `price`

Create:

- `Electronics`
- `Clothing`
- `Food`

Each should calculate its final price differently.

Tax rules:

- Electronics → 15%
- Clothing → 10%
- Food → 5%

Each class should implement:

```python
calculate_final_price()
```

Store different products in one list and calculate their prices using polymorphism.

**Concepts:** inheritance, method overriding, polymorphism.

**Status:** ⬜ Not Started

---

## 20. Employee Management System

Build a small OOP-based employee management system.

Create:

```text
Employee
Manager
Developer
Intern
Company
```

### Employee

Attributes:

- `name`
- `employee_id`
- `salary`

Methods:

- `display_info()`
- `calculate_bonus()`

### Manager

Gets a 20% bonus.

### Developer

Gets a 15% bonus.

### Intern

Gets a 5% bonus.

### Company

Maintain a list of employees and create:

- `add_employee()`
- `remove_employee()`
- `display_employees()`
- `calculate_total_salary()`
- `calculate_total_bonuses()`
- `find_employee(employee_id)`

Example:

```text
Employees:
Ali - Manager - 100000
Ahmed - Developer - 80000
Sara - Intern - 30000

Total Salary: 210000
Total Bonuses: 35000
```

### Concepts Expected

This final exercise combines:

- `__init__`
- Instance attributes
- Instance methods
- Class attributes
- `@classmethod`
- `@staticmethod`
- Encapsulation
- Inheritance
- Method overriding
- Polymorphism
- `super()`
- Lists of objects
- `__str__()`

**Status:** ⬜ Not Started

---

# 📈 Recommended Progression

### Easy

```text
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
```

### Intermediate

```text
11 → 12 → 13 → 16 → 17 → 14 → 15 → 18 → 19 → 20
```

The progression moves from:

```text
Basic Classes
      ↓
Instance Attributes & Methods
      ↓
Object State & Validation
      ↓
Inheritance
      ↓
Encapsulation
      ↓
Class & Static Methods
      ↓
Operator Overloading
      ↓
Polymorphism
      ↓
Real-world OOP System
```

---

# 📊 Progress Tracker

| Level           | Completed |  Total |
| --------------- | --------: | -----: |
| 🟢 Easy         |         7 |     10 |
| 🟡 Intermediate |         0 |     10 |
| **Overall**     |     **7** | **20** |

**Overall Progress: 35%**

---

## 🗂️ File Structure

```text
20-python-oop-practice/
│
├── README.md
├── 01-class.py
├── 02-student.py
├── 03-rectangle.py
├── 04-bank-account.py
├── 05-car.py
├── 06-circle.py
├── 07-employee.py
├── 08-book.py
├── 09-counter.py
├── 10-temperature.py
├── 11-employee-inheritance.py
├── 12-animal-polymorphism.py
├── 13-private-bank-account.py
├── 14-shopping-cart.py
├── 15-library-management.py
├── 16-employee-count.py
├── 17-email-validation.py
├── 18-vector.py
├── 19-ecommerce-product.py
└── 20-employee-management.py
```

---

## 🎯 Goal

Complete all 20 problems while understanding **why each OOP concept is used**, rather than simply memorizing the syntax.

The goal is to become comfortable designing small Python programs using objects, classes, inheritance, encapsulation, and polymorphism.
