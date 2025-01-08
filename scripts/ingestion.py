import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to the {self.dbname} database!")
        except (Exception, psycopg2.Error) as error:
            print(f"Error while connecting to {self.dbname}:", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the PostgreSQL database.")

    def execute_extract_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def execute_load_query(self, query):
        try:
            self.curlsor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except (Exception, psycopg2.Error) as error:
            self.connection.rollback()
            print("Error executing write query:", error)

    def create_a_new_db(self, db_name):
        try:
            # Set the isolation level to autocommit to allow CREATE DATABASE
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Check if the database already exists
            self.cursor.execute(
                sql.SQL("SELECT 1 FROM pg_database WHERE datname = {}").format(
                    sql.Literal(db_name)
                )
            )
            if self.cursor.fetchone():
                print(f"The database '{db_name}' already exists.")
            else:
                # Create the new database
                self.cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
                )
                print(f"Database '{db_name}' created successfully.")

            # Close the connection to the current database
            self.cursor.close()
            self.connection.close()

            # Connect to the newly created (or existing) database
            try:
                self.dbname = db_name
                self.connect()  # Assuming you have a connect method that reconnects
                print(f"Connected to the database: {db_name}")
            except Exception as error:
                print(f"Couldn't connect to the new database '{db_name}': {error}")

        except Exception as error:
            print(f"Couldn't create or connect to the database '{db_name}': {error}")
        finally:
            # Reset isolation level to default (optional)
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


    def execute_sql_file(self, sql_file_path):
        """
        Execute an SQL file using psycopg2.

        Args:
            database_config (dict): Database configuration with keys `dbname`, `user`, `password`, `host`, and `port`.
            sql_file_path (str): Path to the SQL file to execute.
        """
        try:
            # Connect to the PostgreSQL database

            # Open and read the SQL file
            with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()

            # Split the SQL script into individual statements
            sql_statements = sql_script.split(";")

            for statement in sql_statements:
                # Clean up the statement (strip whitespace) and skip empty lines or comments
                cleaned_statement = statement.strip()
                if (cleaned_statement=='') or cleaned_statement.startswith("--") or cleaned_statement.startswith("/") or cleaned_statement.startswith("*"):
                    continue

                if "DROP DATABASE" in cleaned_statement or "CREATE DATABASE" in cleaned_statement:
                    # Enable autocommit for database-level operations
                    self.connection.autocommit = True
                    print(f"Executing (autocommit): {cleaned_statement}")
                    self.cursor.execute(cleaned_statement)
                    self.connection.autocommit = False  # Revert back to transactional mode
                else:
                    # Execute other statements within a transaction
                    print(f"Executing: {cleaned_statement}")
                    self.cursor.execute(cleaned_statement)
            
            self.connection.commit()
            print(f"SQL script from {sql_file_path} executed successfully.")

        except (Exception, psycopg2.Error) as error:
            self.connection.rollback()
            print(f"Error while executing the SQL file: {error}")
        finally:
            # Close the database connection
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection closed.")

# Example usage
if __name__ == "__main__":
    # Database configuration
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123',
        'host': 'localhost',
        'port': 5432
    }
    db_connection = PostgreSQLConnection(**db_config)
    db_connection.connect()
    # Path to the SQL file
    sql_file = './data/raw/Chinook_PostgreSql.sql'
    # db_connection.execute_load_query(sql_file)

    # Execute the SQL file that creats original database schema
    db_connection.create_a_new_db("digital_store_DWH")
    db_connection.execute_sql_file(sql_file)
