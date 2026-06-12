class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []  # Private
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            return f"Grade added successfully: {grade}"
        return "Grade must be between 0 and 100"

    @property
    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)
    
    # Read-only — no setter
    @average.setter
    def average(self, value):
        raise AttributeError("Average is read-only and cannot be set directly")


# Test
s = Student("Ahmed")
s.add_grade(90)
s.add_grade(80)
s.add_grade(100)
print(s.average(38.9))  # 90.0

# s.average = 95  # AttributeError! 🛑
