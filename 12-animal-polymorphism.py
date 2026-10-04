# 12. Animal Polymorphism 🐶🐱🐮
# Create a base class:
#     Animal
# with a method:
#     speak()
# Create:
#     Dog
#     Cat
#     Cow
# Each class should override speak() .
# Expected:
#     Dog: Woof
#     Cat: Meow
#     Cow: Moo
# Then create a list containing different animals and call speak() using a loop.
# Practice: polymorphism.

class Animal:
    def speak(self):
        return "Make Sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof"    
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Cow(Animal):
    def speak(self):
        return "Moo"
    
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    cow = Cow()

    animals = [dog, cat, cow]

    for animal in animals:
        print(animal.speak())