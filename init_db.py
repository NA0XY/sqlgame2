import sqlite3
import os

DATABASE = 'sql_murder_mystery.db'

def init_db():
    """Initialize the database with schema and data"""
    # Remove existing database if it exists
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print(f"Removed existing database: {DATABASE}")
    
    # Create a new database connection
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    # Execute schema.sql to create tables
    try:
        with open('database/schema.sql', 'r') as f:
            schema_script = f.read()
        cursor.executescript(schema_script)
        print("Schema created successfully")
    except Exception as e:
        print(f"Error creating schema: {e}")
        connection.close()
        return
    
    # Execute data.sql to populate tables
    try:
        with open('database/data.sql', 'r') as f:
            data_script = f.read()
        cursor.executescript(data_script)
        connection.commit()
        print("Data imported successfully")
    except Exception as e:
        print(f"Error importing data: {e}")
    
    connection.close()
    print(f"Database {DATABASE} initialized successfully")

if __name__ == "__main__":
    init_db()
