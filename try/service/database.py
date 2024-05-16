import pyodbc

class Database:
    def __init__(self):
        server_name = "MSI\\SQLEXPRESS"
        database_name = "payxpert"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

