from services import PayrollService


def main():
    payroll = PayrollService()

    while True:
        print("\n" + "=" * 50)
        print("  EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  1. Show all employees")
        print("  2. Add employee")
        print("  3. Remove employee")
        print("  4. Add performance review")
        print("  5. Show payroll report")
        print("  6. Polymorphism demo")
        print("  7. Encapsulation test")
        print("  0. Exit")
        print("=" * 50)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            payroll.show_employees()
        elif choice == "2":
            payroll.input_employee()
        elif choice == "3":
            emp_id = input("\nEnter Employee ID to remove: ").strip()
            if payroll.remove_employee(emp_id):
                print(f"Employee {emp_id} removed.")
            else:
                print("Employee not found.")
        elif choice == "4":
            payroll.input_review()
        elif choice == "5":
            print("\n" + payroll.generate_payroll_report())
        elif choice == "6":
            payroll.polymorphism_demo()
        elif choice == "7":
            payroll.encapsulation_test()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
