# 10. Temperature Class
# Create a Temperature class with:
#     celsius
# Create methods:
#     to_fahrenheit()
#     to_kelvin()
# Use the appropriate conversion formulas.

class Temperature:
    
    def __init__(self, celsius):
        self.celsius = celsius
        
    def to_fahrenheit(self):
        return round(((self.celsius * 1.8) + 32), 2)
    
    def to_kelvin(self):
        return round((self.celsius + 273.15), 2)
    
if __name__ == "__main__":
    celsius = 29
    temperature = Temperature(celsius)
    print(f"C: {celsius}\tF: {temperature.to_fahrenheit()}")
    print(f"C: {celsius}\tK: {temperature.to_kelvin()}")
    
    