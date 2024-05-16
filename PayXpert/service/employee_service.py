from interfaces.i_employee_service import IEmployeeService
from model.employee import Employee

class EmployeeService(IEmployeeService):
    def __init__(self):
        self.employees = {}  # In-memory database to store employees

    def get_employee_by_id(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return None

    def get_all_employees(self):
        return list(self.employees.values())

    def add_employee(self, employee):
        if employee.EmployeeID not in self.employees:
            self.employees[employee.EmployeeID] = employee
            return True
        else:
            return False  # Employee with same ID already exists

    def update_employee(self, employee):
        if employee.EmployeeID in self.employees:
            self.employees[employee.EmployeeID] = employee
            return True
        else:
            return False  # Employee with given ID not found

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False  # Employee with given ID not found
