from ingestion import PostgreSQLConnection

if __name__ == "__main__":
    # Database configuration
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123', # User postgres password
        'host': 'localhost',
        'port': 5432
    }

    db_connection = PostgreSQLConnection(**db_config)
    db_connection.connect()

    # Path to the SQL file
    sql_file = '../sql/queries.sql'

    # Execute the SQL file that creates data warehouse schema
    db_connection.execute_sql_file(sql_file)
