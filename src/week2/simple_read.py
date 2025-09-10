import psycopg2

conn = psycopg2.connect(
    dbname="lab_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT id, name, age FROM students;")

rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()