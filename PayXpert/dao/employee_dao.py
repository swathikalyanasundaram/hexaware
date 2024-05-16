from model.employee import Employee
from service.database_context import DatabaseContext

class EmployeeDAO:
    def __init__(self):
        self.db = DatabaseContext()

    def get_employee_by_id(self, employee_id):
        query = "SELECT * FROM Employee WHERE EmployeeID = ?"
        params = (employee_id,)
        result = self.db.execute_query(query, params)
        if result:
            # Assuming result is a single row containing employee data
            employee_data = result[0]
            return Employee(*employee_data)
        else:
            return None

    def get_all_employees(self):
        query = "SELECT * FROM Employee"
        result = self.db.execute_query(query)
        employees = []
        for row in result:
            employees.append(Employee(*row))
        return employees

    def add_employee(self, employee_data):
        query = "INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (employee_data.EmployeeID, employee_data.FirstName, employee_data.LastName, employee_data.DateOfBirth,
                  employee_data.Gender, employee_data.Email, employee_data.PhoneNumber, employee_data.Address,
                  employee_data.Position, employee_data.JoiningDate, employee_data.TerminationDate)
        return self.db.execute_query(query, params)

    def update_employee(self, employee_data):
        query = "UPDATE Employee SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, " \
                "PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ? WHERE EmployeeID = ?"
        params = (employee_data.FirstName, employee_data.LastName, employee_data.DateOfBirth,
                  employee_data.Gender, employee_data.Email, employee_data.PhoneNumber, employee_data.Address,
                  employee_data.Position, employee_data.JoiningDate, employee_data.TerminationDate,
                  employee_data.EmployeeID)
        return self.db.execute_query(query, params)

    def remove_employee(self, employee_id):
        query = "DELETE FROM Employee WHERE EmployeeID = ?"
        params = (employee_id,)
        return self.db.execute_query(query, params)
