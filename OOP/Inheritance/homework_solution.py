class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def working(self):
        return f"{self.name} works at the company"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} writes code in {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} manages a team of {self.team_size} people"


dev = Developer("Ahmed", 8000, "Python")
mgr = Manager("Sara", 12000, 5)

print(dev.work(), ' - ', dev.working())
print(mgr.work(), ' - ', mgr.working())
