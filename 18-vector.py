# 18. Operator Overloading ➕
# Create a Vector class with:
#     x
#     y
# Create two objects:
#     v1 = Vector(2, 3)
#     v2 = Vector(4, 5)
# Allow:
#     v3 = v1 + v2
# to produce:
#     Vector(6, 8)
# Implement:
#     __add__()
# Also implement:
#     __str__()
# so:
#     print(v3)
# outputs:
#     (6, 8)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x, self.y}"
    
    
if __name__ == '__main__':
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    
    v3 = v1 + v2
    
    print(v1)
    print(v2)
    print(v3)