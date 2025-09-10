import psycopg2

try:
    conn = psycopg2.connect(
        dbname="lab_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    print("Connection opened successfully!")

finally:
    if conn:
        conn.close()
        print("Connection closed.")