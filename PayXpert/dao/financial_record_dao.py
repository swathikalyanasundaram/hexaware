import pyodbc
from service.database_context import DatabaseContext
from model.financial_record import FinancialRecord

class FinancialRecordDAO:
    def __init__(self):
        self.db = DatabaseContext()

    def get_financial_record_by_id(self, record_id):
        query = "SELECT * FROM FinancialRecord WHERE RecordID = ?"
        params = (record_id,)
        result = self.db.execute_query(query, params)
        if result:
            # Assuming result is a single row containing financial record data
            financial_record_data = result[0]
            return FinancialRecord(*financial_record_data)
        else:
            return None

    def get_financial_records_for_employee(self, employee_id):
        query = "SELECT * FROM FinancialRecord WHERE EmployeeID = ?"
        params = (employee_id,)
        result = self.db.execute_query(query, params)
        financial_records = []
        for row in result:
            financial_records.append(FinancialRecord(*row))
        return financial_records

    def get_financial_records_for_date(self, record_date):
        query = "SELECT * FROM FinancialRecord WHERE RecordDate = ?"
        params = (record_date,)
        result = self.db.execute_query(query, params)
        financial_records = []
        for row in result:
            financial_records.append(FinancialRecord(*row))
        return financial_records

    def add_financial_record(self, financial_record_data):
        query = "INSERT INTO FinancialRecord VALUES (?, ?, ?, ?, ?, ?)"
        params = (financial_record_data.RecordID, financial_record_data.EmployeeID, financial_record_data.RecordDate,
                  financial_record_data.Description, financial_record_data.Amount, financial_record_data.RecordType)
        return self.db.execute_query(query, params)

    def update_financial_record(self, financial_record_data):
        query = "UPDATE FinancialRecord SET EmployeeID = ?, RecordDate = ?, Description = ?, Amount = ?, " \
                "RecordType = ? WHERE RecordID = ?"
        params = (financial_record_data.EmployeeID, financial_record_data.RecordDate, financial_record_data.Description,
                  financial_record_data.Amount, financial_record_data.RecordType, financial_record_data.RecordID)
        return self.db.execute_query(query, params)

    def remove_financial_record(self, record_id):
        query = "DELETE FROM FinancialRecord WHERE RecordID = ?"
        params = (record_id,)
        return self.db.execute_query(query, params)
