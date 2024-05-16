import pyodbc
from employee_service import EmployeeService
from payroll_service import PayrollService
from tax_service import TaxService
from financial_record_service import FinancialRecordService
from mainmenu import MainMenu

server_name = "MSI\\SQLEXPRESS"
database_name = "payxpert"

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

if __name__ == "__main__":
    MainMenu.main_menu(cursor, conn)
