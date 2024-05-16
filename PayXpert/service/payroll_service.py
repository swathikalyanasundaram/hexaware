from interfaces.i_payroll_service import IPayrollService
from model.payroll import Payroll

class PayrollService(IPayrollService):
    def generate_payroll(self, employee_id, pay_period_start_date, pay_period_end_date):
        pass

    def get_payroll_by_id(self, payroll_id):
        pass

    def get_payrolls_for_employee(self, employee_id):
        pass

    def get_payrolls_for_period(self, start_date, end_date):
        pass
