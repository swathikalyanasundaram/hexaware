

import pyodbc  # Example, use appropriate library for your database

class DBConnUtil:
    @staticmethod
    def get_connection(property_string):
        # Implement method to establish a database connection using the property string
        connection = pyodbc.connect(property_string)
        return connection
