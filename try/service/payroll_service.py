import pyodbc
from datetime import datetime

class PayrollService:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def read_payrolls(self):
        self.cursor.execute("SELECT * FROM Payroll")
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def generate_payroll(self, employee_id, start_date, end_date):
        
        self.cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
        employee = self.cursor.fetchone()

        # Perform payroll calculations
        basic_salary = 2000  # Example basic salary
        overtime_hours = 10  # Example overtime hours
        overtime_rate = 20  # Example overtime rate per hour
        deductions = 500  # Example deductions

        net_salary = basic_salary + (overtime_hours * overtime_rate) - deductions

        # Insert payroll data into the database
        self.cursor.execute(
            """
            INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimeHours, OvertimeRate, Deductions, NetSalary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (employee_id, start_date, end_date, basic_salary, overtime_hours, overtime_rate, deductions, net_salary),
        )
        self.conn.commit()

        print("Payroll generated successfully.")


    def get_payroll_by_id(self, payroll_id):
        self.cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
        payroll = self.cursor.fetchone()
        print(payroll)

    def get_payrolls_for_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def get_payrolls_for_period(self, start_date, end_date):
        query = f"""
            SELECT * 
            FROM Payroll 
            WHERE PayPeriodStartDate >= '{start_date}' AND PayPeriodEndDate <= '{end_date}'
        """
        self.cursor.execute(query)
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)