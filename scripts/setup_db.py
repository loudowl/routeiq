import psycopg2
from psycopg2 import sql

# Connect to your postgres DB
conn = psycopg2.connect("dbname=routeiq_db user=user password=password")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("""
    CREATE TABLE IF NOT EXISTS request_logs (
        id SERIAL PRIMARY KEY,
        model_used VARCHAR(255),
        tokens INTEGER,
        latency FLOAT,
        estimated_cost FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
