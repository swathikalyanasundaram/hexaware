import pyodbc
from service.database_context import DatabaseContext
from model.payroll import Payroll

class PayrollDAO:
    def __init__(self):
        self.db = DatabaseContext()

    def get_payroll_by_id(self, payroll_id):
        query = "SELECT * FROM Payroll WHERE PayrollID = ?"
        params = (payroll_id,)
        result = self.db.execute_query(query, params)
        if result:
            # Assuming result is a single row containing payroll data
            payroll_data = result[0]
            return Payroll(*payroll_data)
        else:
            return None

    def get_payrolls_for_employee(self, employee_id):
        query = "SELECT * FROM Payroll WHERE EmployeeID = ?"
        params = (employee_id,)
        result = self.db.execute_query(query, params)
        payrolls = []
        for row in result:
            payrolls.append(Payroll(*row))
        return payrolls

    def get_payrolls_for_period(self, start_date, end_date):
        query = "SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?"
        params = (start_date, end_date)
        result = self.db.execute_query(query, params)
        payrolls = []
        for row in result:
            payrolls.append(Payroll(*row))
        return payrolls

    def add_payroll(self, payroll_data):
        query = "INSERT INTO Payroll VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        params = (payroll_data.PayrollID, payroll_data.EmployeeID, payroll_data.PayPeriodStartDate,
                  payroll_data.PayPeriodEndDate, payroll_data.BasicSalary, payroll_data.OvertimePay,
                  payroll_data.Deductions, payroll_data.NetSalary)
        return self.db.execute_query(query, params)

    def update_payroll(self, payroll_data):
        query = "UPDATE Payroll SET EmployeeID = ?, PayPeriodStartDate = ?, PayPeriodEndDate = ?, " \
                "BasicSalary = ?, OvertimePay = ?, Deductions = ?, NetSalary = ? WHERE PayrollID = ?"
        params = (payroll_data.EmployeeID, payroll_data.PayPeriodStartDate, payroll_data.PayPeriodEndDate,
                  payroll_data.BasicSalary, payroll_data.OvertimePay, payroll_data.Deductions,
                  payroll_data.NetSalary, payroll_data.PayrollID)
        return self.db.execute_query(query, params)

    def remove_payroll(self, payroll_id):
        query = "DELETE FROM Payroll WHERE PayrollID = ?"
        params = (payroll_id,)
        return self.db.execute_query(query, params)
