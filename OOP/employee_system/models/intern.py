from models import Employee
from datetime import date


class Intern(Employee):
    
    def __init__(
        self,
        name: str,
        email: str,
        birth_date: date,
        employee_id: str,
        hire_date: date,
        stipend: float,
        mentor: Employee = None
    ):
        super().__init__(name, email, birth_date, employee_id, hire_date, stipend)
        self._mentor = mentor
    
    @property
    def mentor(self) -> Employee:
        return self._mentor
    
    @mentor.setter
    def mentor(self, value: Employee):
        if not isinstance(value, Employee):
            raise ValueError("The mentor must be an employee")
        self._mentor = value
    
    def calculate_bonus(self) -> float:
        return self.average_performance() * 200
    
    def get_role(self) -> str:
        return "Intern"