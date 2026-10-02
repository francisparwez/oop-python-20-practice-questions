# 6. Circle Class
# Create a Circle class with:
#     radius
# Create methods:
#     area()
#     circumference()
# Use:
#     π = 3.14159

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