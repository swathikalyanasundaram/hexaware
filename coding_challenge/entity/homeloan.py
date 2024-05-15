from loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None, loan_status=None, property_address=None, property_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", loan_status)
        self.property_address = property_address
        self.property_value = property_value
    
    # Getters and Setters
    def get_property_address(self):
        return self.property_address

    def set_property_address(self, property_address):
        self.property_address = property_address

    # Repeat the above pattern for other attributes

    def print_home_loan_info(self):
        super().print_loan_info()
        print("Property Address:", self.property_address)
        print("Property Value:", self.property_value)
