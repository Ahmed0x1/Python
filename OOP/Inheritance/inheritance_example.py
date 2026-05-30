# Create a parent class called Employee
# - Attributes: name, salary
# - Method: working() returns a general statement about working at the company

# Create a child class Developer that inherits from Employee
# - Adds attribute: programming_language
# - Overrides work() to show the developer writes code in a specific language

# Create a child class Manager that inherits from Employee
# - Adds attribute: team_size
# - Overrides work() to show the manager manages a team of a certain size

# Instantiate objects from Developer and Manager
# - Call work() and working() to demonstrate general vs specialized behavior


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    def eat(self):
        return f"{self.name} eats fish"

class Dog(Animal):
    def eat(self):
        return f"{self.name} eats bones"


array = [Dog("Billy"), Cat("jessy")]
for a in array:
    print(a.eat(), ' - ', a.speak())

