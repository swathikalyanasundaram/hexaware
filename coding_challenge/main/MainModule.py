import sys
import os

# Append the parent directory of the current file to sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from coding_challenge.dao.IloanRepositoryImpl import ILoanRepositoryImpl




class MainModule():

   

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
                # Apply for a loan
                pass
            elif choice == "2":
                # Calculate interest
                pass
            elif choice == "3":
                # Check loan status
                pass
            elif choice == "4":
                # Calculate EMI
                pass
            elif choice == "5":
                # Make loan repayment
                pass
            elif choice == "6":
                # Get all loans
                pass
            elif choice == "7":
                # Get loan by ID
                pass
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
