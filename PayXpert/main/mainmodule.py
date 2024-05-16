from service.employee_service import EmployeeService
from model.employee import Employee

class MainModule:
    def __init__(self):
        self.employee_service = EmployeeService()

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. View Employee by ID")
        print("5. View All Employees")
        print("6. Exit")

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        new_employee = Employee(employee_id, first_name, last_name)
        success = self.employee_service.add_employee(new_employee)
        if success:
            print("Employee added successfully!")
        else:
            print("Failed to add employee. Employee ID already exists.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        employee = self.employee_service.get_employee_by_id(employee_id)
        if employee:
            # Collect updated employee details...
            updated_employee = Employee(employee_id, first_name=None, last_name=None)
            success = self.employee_service.update_employee(updated_employee)
            if success:
                print("Employee updated successfully!")
            else:
                print("Failed to update employee.")
        else:
            print("Employee not found.")

    def remove_employee(self):
        employee_id = input("Enter Employee ID to remove: ")
        success = self.employee_service.remove_employee(employee_id)
        if success:
            print("Employee removed successfully!")
        else:
            print("Failed to remove employee. Employee ID not found.")

    def view_employee_by_id(self):
        employee_id = input("Enter Employee ID to view: ")
        employee = self.employee_service.get_employee_by_id(employee_id)
        if employee:
            print("Employee Details:")
            print(employee.__dict__)  # Display employee details
        else:
            print("Employee not found.")

    def view_all_employees(self):
        employees = self.employee_service.get_all_employees()
        if employees:
            print("All Employees:")
            for employee in employees:
                print(employee.__dict__)  # Display employee details
        else:
            print("No employees found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.update_employee()
            elif choice == "3":
                self.remove_employee()
            elif choice == "4":
                self.view_employee_by_id()
            elif choice == "5":
                self.view_all_employees()
            elif choice == "6":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
