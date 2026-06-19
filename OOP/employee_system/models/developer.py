from models import Employee
from datetime import date
from typing import List, Set


class Developer(Employee):
    
    def __init__(
        self,
        name: str,
        email: str,
        birth_date: date,
        employee_id: str,
        hire_date: date,
        base_salary: float,
        skills: List[str] = None
    ):
        super().__init__(name, email, birth_date, employee_id, hire_date, base_salary)
        self._skills: Set[str] = set(skills or [])
    
    def add_skill(self, skill: str):
        self._skills.add(skill.lower())
    
    def has_skill(self, skill: str) -> bool:
        return skill.lower() in self._skills
    
    @property
    def skills(self) -> List[str]:
        return sorted(self._skills)
    
    def calculate_bonus(self) -> float:
        skill_bonus = len(self._skills) * 100
        experience_bonus = self.years_of_service * 200
        performance_multiplier = 1 + (self.average_performance() / 10)
        return (skill_bonus + experience_bonus) * performance_multiplier
    
    def get_role(self) -> str:
        return "Developer"
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Skills: {', '.join(self._skills)}"