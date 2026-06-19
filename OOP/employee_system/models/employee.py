from models import Person
from abc import ABC, abstractmethod
from datetime import date
from typing import List


class Employee(Person, ABC):

    def __init__(
        self, 
        name: str, 
        email: str, 
        birth_date: date,
        employee_id: str,
        hire_date: date,
        base_salary: float
    ):
        super().__init__(name, email, birth_date)
        self._employee_id = employee_id
        self._hire_date = hire_date
        self.__base_salary = base_salary 
        self._performance_reviews: List[float] = []
    
    @property
    def employee_id(self) -> str:
        return self._employee_id
    
    @property
    def base_salary(self) -> float:
        return self.__base_salary
    
    @base_salary.setter
    def base_salary(self, value: float):
        if value < 0:
            raise ValueError("the salary cannot be negative")
        self.__base_salary = value
    
    @property
    def years_of_service(self) -> int:
        today = date.today()
        return today.year - self._hire_date.year
    
    def add_performance_review(self, score: float):
        if not 0 <= score <= 5:
            raise ValueError("the score must be between 0 and 5")
        self._performance_reviews.append(score)
    
    def average_performance(self) -> float:
        if not self._performance_reviews:
            return 0.0
        return sum(self._performance_reviews) / len(self._performance_reviews)
    
    @abstractmethod
    def calculate_bonus(self) -> float:
        pass
    
    def total_compensation(self) -> float:
        return self.__base_salary + self.calculate_bonus()
    
    def get_role(self) -> str:
        return "Employee"