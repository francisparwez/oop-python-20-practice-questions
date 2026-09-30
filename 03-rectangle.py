# 3. Rectangle Class
# Create a Rectangle class with:
#     length
#     width
# Create methods:
#     area()
#     perimeter()
# Example:
#     Area: 50
#     Perimeter: 30

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