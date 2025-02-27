# pip install psycopg2-binary

import psycopg2

# Database connection parameters
host = ''
port = ''  # Added the correct port
database = ''
user = ''
password = ''


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cursor = conn.cursor()

# Query to get the schema of a specific table
table_name = ''
query = f"""
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = '{table_name}';
"""

# Execute the query
cursor.execute(query)

# Fetch and print the results
schema = cursor.fetchall()
for column in schema:
    print(f"Column: {column[0]}, Data Type: {column[1]}, Is Nullable: {column[2]}")

# Close the cursor and connection
cursor.close()
conn.close()