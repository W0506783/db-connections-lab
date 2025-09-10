import psycopg2

def delete_student(student_id):
    conn = psycopg2.connect(
        dbname="lab_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s;", (student_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_student(2)
    print("Deleted student with ID 2")