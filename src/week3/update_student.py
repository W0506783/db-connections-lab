import psycopg2

def update_student_age(student_id, new_age):
    conn = psycopg2.connect(
        dbname="lab_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("UPDATE students SET age = %s WHERE id = %s;", (new_age, student_id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_student_age(1, 30)
    print("Updated student 1's age to 30")