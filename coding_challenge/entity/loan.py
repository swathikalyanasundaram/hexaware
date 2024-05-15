class Loan:
   
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None, loan_type=None, loan_status=None):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status
    
   
    def get_loan_id(self):
        return self.loan_id

    def set_loan_id(self, loan_id):
        self.loan_id = loan_id

   

    def print_loan_info(self):
        print("Loan ID:", self.loan_id)
        print("Customer:", self.customer)
        print("Principal Amount:", self.principal_amount)
        print("Interest Rate:", self.interest_rate)
        print("Loan Term:", self.loan_term)
        print("Loan Type:", self.loan_type)
        print("Loan Status:", self.loan_status)
