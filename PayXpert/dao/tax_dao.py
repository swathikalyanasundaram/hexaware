import pyodbc
from service.database_context import DatabaseContext
from model.tax import Tax

class TaxDAO:
    def __init__(self):
        self.db = DatabaseContext()

    def get_tax_by_id(self, tax_id):
        query = "SELECT * FROM Tax WHERE TaxID = ?"
        params = (tax_id,)
        result = self.db.execute_query(query, params)
        if result:
            # Assuming result is a single row containing tax data
            tax_data = result[0]
            return Tax(*tax_data)
        else:
            return None

    def get_taxes_for_employee(self, employee_id):
        query = "SELECT * FROM Tax WHERE EmployeeID = ?"
        params = (employee_id,)
        result = self.db.execute_query(query, params)
        taxes = []
        for row in result:
            taxes.append(Tax(*row))
        return taxes

    def get_taxes_for_year(self, tax_year):
        query = "SELECT * FROM Tax WHERE TaxYear = ?"
        params = (tax_year,)
        result = self.db.execute_query(query, params)
        taxes = []
        for row in result:
            taxes.append(Tax(*row))
        return taxes

    def calculate_tax(self, employee_id, tax_year):
        # Implement logic to calculate tax for a specific employee and year
        # This can be a complex calculation based on the employee's income, deductions, and tax brackets
        pass

    def add_tax(self, tax_data):
        query = "INSERT INTO Tax VALUES (?, ?, ?, ?)"
        params = (tax_data.TaxID, tax_data.EmployeeID, tax_data.TaxYear, tax_data.TaxAmount)
        return self.db.execute_query(query, params)

    def update_tax(self, tax_data):
        query = "UPDATE Tax SET EmployeeID = ?, TaxYear = ?, TaxAmount = ? WHERE TaxID = ?"
        params = (tax_data.EmployeeID, tax_data.TaxYear, tax_data.TaxAmount, tax_data.TaxID)
        return self.db.execute_query(query, params)
