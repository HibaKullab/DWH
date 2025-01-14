from ingestion import PostgreSQLConnection


if __name__ == "__main__":
    # Database configuration
    db_config = {
        'dbname': 'digital_store_DWH',
        'user': 'postgres',
        'password': '123', # User postgres password
        'host': 'localhost',
        'port': 5432
    }

    db_connection = PostgreSQLConnection(**db_config)
    db_connection.connect()
