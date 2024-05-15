from IloanRepository import ILoanRepository
from DBConnUtil import DBConnection
from ex import InvalidLoanException

class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.db_connection = DBConnection()

    def applyLoan(self, loan):
        try:
            self.db_connection.cursor.execute("INSERT INTO loans (loanId, customerId, principalAmount, interestRate, loanTerm, loanType, loanStatus) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                           (loan.loanId, loan.customer.customerId, loan.principalAmount, loan.interestRate, loan.loanTerm, loan.loanType, "Pending"))
            self.db_connection.conn.commit()
        except Exception as e:
            self.db_connection.conn.rollback()
            raise e
        finally:
            self.db_connection.close()

    def calculateInterest(self, loanId):
        try:
            self.db_connection.cursor.execute("SELECT principalAmount, interestRate, loanTerm FROM loans WHERE loanId = ?", (loanId,))
            loan_data = self.db_connection.cursor.fetchone()
            if loan_data:
                principalAmount, interestRate, loanTerm = loan_data
                interest = (principalAmount * interestRate * loanTerm) / 12
                return interest
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()

    def loanStatus(self, loanId):
        try:
            self.db_connection.cursor.execute("SELECT creditScore FROM loans WHERE loanId = ?", (loanId,))
            credit_score = self.db_connection.cursor.fetchone()[0]
            if credit_score > 650:
                return "Loan Approved"
            else:
                return "Loan Rejected"
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()

    def calculateEMI(self, loanId):
        try:
            self.db_connection.cursor.execute("SELECT principalAmount, interestRate, loanTerm FROM loans WHERE loanId = ?", (loanId,))
            loan_data = self.db_connection.cursor.fetchone()
            if loan_data:
                principalAmount, interestRate, loanTerm = loan_data
                monthly_interest_rate = interestRate / 12 / 100
                emi = (principalAmount * monthly_interest_rate * ((1 + monthly_interest_rate) ** loanTerm)) / (((1 + monthly_interest_rate) ** loanTerm) - 1)
                return emi
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()

    def loanRepayment(self, loanId, amount):
        try:
            self.db_connection.cursor.execute("SELECT principalAmount, interestRate, loanTerm FROM loans WHERE loanId = ?", (loanId,))
            loan_data = self.db_connection.cursor.fetchone()
            if loan_data:
                principalAmount, interestRate, loanTerm = loan_data
                monthly_interest_rate = interestRate / 12 / 100
                emi = (principalAmount * monthly_interest_rate * ((1 + monthly_interest_rate) ** loanTerm)) / (((1 + monthly_interest_rate) ** loanTerm) - 1)
                no_of_emi_paid = amount / emi
                return no_of_emi_paid
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()

    def getAllLoan(self):
        try:
            self.db_connection.cursor.execute("SELECT * FROM loans")
            loans = self.db_connection.cursor.fetchall()
            return loans
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()

    def getLoanById(self, loanId):
        try:
            self.db_connection.cursor.execute("SELECT * FROM loans WHERE loanId = ?", (loanId,))
            loan = self.db_connection.cursor.fetchone()
            if loan:
                return loan
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            raise e
        finally:
            self.db_connection.close()
