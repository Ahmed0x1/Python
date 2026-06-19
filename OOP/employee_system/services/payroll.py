from typing import List
from datetime import date
from models.employee import Employee
from models.developer import Developer
from models.manager import Manager
from models.intern import Intern


class PayrollService:
    
    def __init__(self):
        self._employees: List[Employee] = []
    
    def add_employee(self, employee: Employee):
        self._employees.append(employee)
    
    def remove_employee(self, employee_id: str) -> bool:
        for i, emp in enumerate(self._employees):
            if emp.employee_id == employee_id:
                self._employees.pop(i)
                return True
        return False
    
    def get_employee(self, employee_id: str) -> Employee:
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def list_employees(self) -> List[Employee]:
        return self._employees
    
    def show_employees(self):
        if not self._employees:
            print("\nNo employees found.")
            return
        print(f"\n{'ID':<10} {'Name':<15} {'Role':<22} {'Salary':>10}")
        print("-" * 60)
        for emp in self._employees:
            print(f"{emp.employee_id:<10} {emp.name:<15} {emp.get_role():<22} ${emp.base_salary:>7,.0f}")

    def input_employee(self):
        print("\n--- Add Employee ---")
        emp_type = input("Type Number (1: Developer, 2: Manager, 3: Intern): ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        emp_id = input("Employee ID: ").strip()

        try:
            year = int(input("Birth year (e.g. 1995): "))
            month = int(input("Birth month (1-12): "))
            day = int(input("Birth day: "))
            birth_date = date(year, month, day)

            hire_year = int(input("Hire year (e.g. 2022): "))
            hire_month = int(input("Hire month (1-12): "))
            hire_day = int(input("Hire day: "))
            hire_date = date(hire_year, hire_month, hire_day)

            salary = float(input("Base salary: "))
        except ValueError:
            print("Invalid date or number.")
            return

        if emp_type == "1":
            skills = input("Skills (comma separated): ").strip()
            skills_list = [s.strip() for s in skills.split(",") if s.strip()]
            emp = Developer(name, email, birth_date, emp_id, hire_date, salary, skills_list)
        elif emp_type == "2":
            department = input("Department: ").strip()
            emp = Manager(name, email, birth_date, emp_id, hire_date, salary, department)
        elif emp_type == "3":
            emp = Intern(name, email, birth_date, emp_id, hire_date, salary)
        else:
            print("Invalid type.")
            return

        self._employees.append(emp)
        print(f"Added: {name} ({emp.get_role()})")

    def input_review(self):
        emp_id = input("\nEnter Employee ID: ").strip()
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return
        try:
            score = float(input("Performance score (0-5): "))
            emp.add_performance_review(score)
            print(f"Review {score} added to {emp.name}. Average: {emp.average_performance():.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    def generate_payroll_report(self) -> str:
        report = ["=" * 60, "PAYROLL REPORT", "=" * 60]
        total = 0
        
        for emp in self._employees:
            comp = emp.total_compensation()
            total += comp
            report.append(
                f"{emp.get_role():<20} | {emp.name:<15} | "
                f"Base: ${emp.base_salary:>8,.0f} | "
                f"Bonus: ${emp.calculate_bonus():>8,.0f} | "
                f"Total: ${comp:>8,.0f}"
            )
        
        report.append("-" * 60)
        report.append(f"{'TOTAL':<20} | {'':15} | {'':15} | {'':15} | ${total:>8,.0f}")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def polymorphism_demo(self):
        if not self._employees:
            print("\nNo employees to demo.")
            return
        print("\nPolymorphism in action:")
        print(f"{'Name':<15} {'Role':<22} {'Bonus':>10}")
        print("-" * 50)
        for emp in self._employees:
            print(f"{emp.name:<15} {emp.get_role():<22} ${emp.calculate_bonus():>7,.0f}")
        print("\nSame loop, same method call, different results!")
    
    def encapsulation_test(self):
        if not self._employees:
            print("\nNo employees to test.")
            return
        print("\nEncapsulation test - trying to set negative salary...")
        emp = self._employees[0]
        try:
            emp.base_salary = -100
        except ValueError as e:
            print(f"Blocked: {e}")
        print(f"{emp.name}'s salary is still ${emp.base_salary:,.0f}")

    def get_team_report(self, manager_id: str) -> str:
        manager = self.get_employee(manager_id)
        if not manager or not hasattr(manager, 'team_size'):
            return "Manager not found"
        return f"Team size: {manager.team_size}"
