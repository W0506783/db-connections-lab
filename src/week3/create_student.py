import psycopg2

def create_student(name, age):
    conn = psycopg2.connect(
        dbname="lab_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
    new_id = cur.fetchone()[0]

    conn.commit()
    conn.close()
    return new_id

if __name__ == "__main__":
    student_id = create_student("Diana", 20)
    print(f"Inserted student with ID {student_id}")