# 19. E-Commerce Product System 💻
# Create a base class:
#     Product
# with:
#     name
#     price
# Create:
#     Electronics
#     Clothing
#     Food
# Each should calculate its final price differently.
# For example:
#     Electronics → 15% tax
#     Clothing → 10% tax
#     Food → 5% tax
# Each class should implement:
#     calculate_final_price()
# Then store different products in one list and calculate their prices using polymorphism.
# Practice: inheritance + overriding + polymorphism.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def calculate_final_price(self):
        raise NotImplementedError("Subclasses Must Implement This Method")
    
class Electronics(Product):
    def calculate_final_price(self):
        return self.price * 1.15
    
class Clothing(Product):
    def calculate_final_price(self):
        return self.price * 1.10

class Food(Product):
    def calculate_final_price(self):
        return self.price * 1.05
    
if __name__ == "__main__":
    products = [
        Electronics("Smart Watch", 200),
        Clothing("Jeans", 50),
        Food("Chocolate", 5)
    ]
    
    for product in products:
        print(f"{product.name}: ${product.calculate_final_price():.2f}")