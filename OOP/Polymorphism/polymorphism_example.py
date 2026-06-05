# Create a payment system:
# - A Payment class with a method pay(self, amount)
# - A CreditCard class that inherits from it and adds a card number
# - A PayPal class that inherits from it and adds an email
# - Each one implements pay() in its own way

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Hau!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says: Moo!"

animals = [Dog("Buddy"), Cat("Luna"), Cow("GG")]
for a in animals:
    print(a.speak())
