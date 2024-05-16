class Payroll:
    def __init__(self, payroll_id, employee_id, pay_period_start_date, pay_period_end_date, basic_salary, overtime_pay, deductions, net_salary):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.pay_period_start_date = pay_period_start_date
        self.pay_period_end_date = pay_period_end_date
        self.basic_salary = basic_salary
        self.overtime_pay = overtime_pay
        self.deductions = deductions
        self.net_salary = net_salary
