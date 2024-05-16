from interfaces.i_financial_records_service import IFinancialRecordService
from model.financial_record import FinancialRecord

class FinancialRecordService(IFinancialRecordService):
    def add_financial_record(self, financial_record):
        pass

    def get_financial_record_by_id(self, record_id):
        pass

    def get_financial_records_for_employee(self, employee_id):
        pass

    def get_financial_records_for_date(self, date):
        pass
