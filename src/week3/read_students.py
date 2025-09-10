import psycopg2

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', age={self.age})"

def get_students():
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
    conn.close()
    return [Student(*row) for row in rows]

if __name__ == "__main__":
    students = get_students()
    print(students)