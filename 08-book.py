# 8. Book Class
# Create a Book class with:
#     title
#     author
#     price
# Create a method:
#     apply_discount(percent)
# that reduces the book price.
# Example:
#     Original price: 1000
#     Discount: 20%
#     New price: 800

class Book:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def apply_discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))
        
    def __str__(self):
        return f"{self.title} by {self.author} priced ${self.price:.2f}"
        
if __name__ == "__main__":
    book1 = Book("Harry Potter", "JK Rowling", 29.99)
    print(book1)
    book1.apply_discount(20)
    print(book1)