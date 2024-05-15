conn_str=(
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_connection=yes"
)


- connection statement
```
conn=pyodbc.connect(conn_str)
cursor=conn.cursor()

cursor.execute("select 1")
print("database connection is successfull")
```