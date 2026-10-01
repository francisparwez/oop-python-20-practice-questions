# 5. Car Class
# Create a Car class with:
#     brand
#     model
#     year
# Create a method:
#     display_info()
# that displays:
#     Toyota Corolla (2022)

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