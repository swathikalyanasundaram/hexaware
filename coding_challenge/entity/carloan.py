from loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None, loan_status=None, car_model=None, car_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", loan_status)
        self.car_model = car_model
        self.car_value = car_value
    
    # Getters and Setters
    def get_car_model(self):
        return self.car_model

    def set_car_model(self, car_model):
        self.car_model = car_model

    # Repeat the above pattern for other attributes

    def print_car_loan_info(self):
        super().print_loan_info()
        print("Car Model:", self.car_model)
        print("Car Value:", self.car_value)
