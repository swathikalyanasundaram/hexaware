from interfaces.i_tax_service import ITaxService
from model.tax import Tax
class TaxService(ITaxService):
    def calculate_tax(self, employee_id, taxable_income):
        pass

    def get_tax_by_id(self, tax_id):
        pass

    def get_taxes_for_employee(self, employee_id):
        pass

    def get_taxes_for_year(self, year):
        pass
