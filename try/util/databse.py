import pyodbc
class databse:

    server_name = "MSI\\SQLEXPRESS"
    database_name = "PayrollManagement"


    conn_str = (
        f"Driver={{SQL Server}};"
        f"Server={server_name};"
        f"Database={database_name};"
        f"Trusted_Connection=yes;"
)
# print(conn_str)
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("Database connection is successful")