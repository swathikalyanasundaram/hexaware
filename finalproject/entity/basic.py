import pyodbc
 
server_name = "MSI\SQLEXPRESS"
database_name = "HexawareMoviesDB"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
 
 
print(conn_str)
 
 
# When new object -> new connection
class DBConnection:
    def __init__(self):
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
 
    def close(self):
        self.cursor.close()
        self.conn.close()