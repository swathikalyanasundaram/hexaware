import pyodbc

# Define the connection string
server = 'MSI\\SQLEXPRESS'
database = 'PayrollManagement'

# If using Windows Authentication
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Establish connection to the SQL Server database
    conn = pyodbc.connect(conn_str)
    print("Connected to the database")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example query execution
    cursor.execute("SELECT * FROM Employee")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()
    print("Connection closed")
    
except Exception as e:
    print(f"Error: {e}")
