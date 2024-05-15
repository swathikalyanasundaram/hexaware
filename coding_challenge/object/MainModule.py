from IloanRepositoryImpl import ILoanRepositoryImpl
from loan import Loan

class MainModule:
    def __init__(self):
        self.loan_repo = ILoanRepositoryImpl()

    def display_menu(self):
        print("Loan Management System")
        print("1. Apply for a loan")
        print("2. Calculate interest")
        print("3. Check loan status")
        print("4. Calculate EMI")
        print("5. Make loan repayment")
        print("6. Get all loans")
        print("7. Get loan by ID")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                loan_id = input("Enter Loan ID: ")
                customer_id = input("Enter Customer ID: ")
                principal_amount = float(input("Enter Principal Amount: "))
                interest_rate = float(input("Enter Interest Rate: "))
                loan_term = int(input("Enter Loan Term (in months): "))
                loan_type = input("Enter Loan Type: ")
                loan = Loan(loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type)
                self.loan_repo.applyLoan(loan)
            elif choice == "2":
                loan_id = input("Enter Loan ID: ")
                interest = self.loan_repo.calculateInterest(loan_id)
                print(f"Interest for loan {loan_id}: {interest}")
            elif choice == "3":
                loan_id = input("Enter Loan ID: ")
                status = self.loan_repo.loanStatus(loan_id)
                print(f"Loan status for loan {loan_id}: {status}")
            elif choice == "4":
                loan_id = input("Enter Loan ID: ")
                emi = self.loan_repo.calculateEMI(loan_id)
                print(f"EMI for loan {loan_id}: {emi}")
            elif choice == "5":
                loan_id = input("Enter Loan ID: ")
                amount = float(input("Enter repayment amount: "))
                no_of_emi_paid = self.loan_repo.loanRepayment(loan_id, amount)
                print(f"Number of EMIs paid for loan {loan_id}: {no_of_emi_paid}")
            elif choice == "6":
                loans = self.loan_repo.getAllLoan()
                print("All loans:")
                for loan in loans:
                    print(loan)
            elif choice == "7":
                loan_id = input("Enter Loan ID: ")
                loan = self.loan_repo.getLoanById(loan_id)
                print(f"Loan details for loan {loan_id}: {loan}")
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
