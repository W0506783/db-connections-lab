import psycopg2

conn = psycopg2.connect(
    dbname="lab_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

student_name = input("Enter student name: ")

# SAFE parameterized query
cur.execute("SELECT * FROM students WHERE name = %s;", (student_name,))

result = cur.fetchall()
print("Result:", result)

conn.close()