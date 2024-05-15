import pyodbc
from propUtil import PropertyUtil


# When new object -> new connection
class DBConnection:
    def __init__(self):
        conn_str = PropertyUtil.get_property_string()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
