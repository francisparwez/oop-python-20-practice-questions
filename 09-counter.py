# 9. Counter Class
# Create a Counter class with an attribute:
#     count = 0
# Create methods:
#     increment()
#     decrement()
#     reset()
#     display()
# Example:
#     0 → 1 → 2 → 1 → 0

class Counter:
    
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def decrement(self):
        if self.count == 0:
            print("The minimum limit of 0 has already been reached.")
        else:            
            self.count -= 1
            
    def reset(self):
        self.count = 0
        
    def display(self):
        print(self.count)
        

if __name__ == '__main__':
    counter = Counter()
    counter.increment()
    counter.display()
    counter.increment()
    counter.display()
    counter.decrement()
    counter.display()
    counter.reset()
    counter.display()
    counter.decrement()
    counter.display()
    counter.increment()
    counter.display()
    