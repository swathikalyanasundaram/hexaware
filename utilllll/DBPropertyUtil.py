class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-DLFEC7O\SQLEXPRESS"
        database_name = "HexawareMoviesDB"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str