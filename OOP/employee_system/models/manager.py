from models import Employee
from datetime import date
from typing import List


class Manager(Employee):
    
    def __init__(
        self,
        name: str,
        email: str,
        birth_date: date,
        employee_id: str,
        hire_date: date,
        base_salary: float,
        department: str,
        team: List[Employee] = None
    ):
        super().__init__(name, email, birth_date, employee_id, hire_date, base_salary)
        self._department = department
        self._team: List[Employee] = team or []
    
    def add_team_member(self, employee: Employee):
        if employee not in self._team:
            self._team.append(employee)
    
    def remove_team_member(self, employee: Employee):
        if employee in self._team:
            self._team.remove(employee)
    
    @property
    def team_size(self) -> int:
        return len(self._team)
    
    @property
    def department(self) -> str:
        return self._department
    
    def calculate_bonus(self) -> float:
        team_bonus = self.team_size * 500
        performance_bonus = self.average_performance() * 1000
        return team_bonus + performance_bonus
    
    def get_role(self) -> str:
        return f"Manager ({self._department})"
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Team: {self.team_size} members"