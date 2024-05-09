import pyodbc

server_name = "MSI\SQLEXPRESS"
database_name = "HexawareMoviesDB"

conn_str = (
    f"driver={{SQL Server}};"
    f"server={server_name};"
    f"database={database_name};"
    f"Trusted_connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("select 1")
print("databse connection is successful ")
print("welcome to the movies app")

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("select 1")
print("Database connection is successful")

def read_movies():
    cursor.execute("Select * from movies")
    movies = cursor.fetchall()
    #for movies in movies:
     #   print(movies)
    for row in cursor:
        print(row)

def create_movie():
    cursor.execute(
        "insert into movies(title,year,directorid) values ('inception',2010,1)"
    )
    conn.commit() 

if __name__ == "__main__":
     read_movies()


