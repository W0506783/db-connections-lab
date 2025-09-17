# Workshop: CRUD Operations with PostgreSQL

**Course:** DBAS 3200 – Data-Driven Application Programming
**Week 3 Focus:** Implementing Create, Read, Update, and Delete operations through a database API, and mapping query results to Python objects.

---

## Learning Outcomes (this workshop supports)

* **Outcome 13:** Perform input/output operations with databases.
* **Outcome 14:** Implement CRUD operations to support application data workflows.

---

## Workshop Activities

### 1. Setup Review

1. Open your `dbas3200-project` repo in **VS Code**.
2. Confirm your `students` table exists from Week 2. If not, run:

   ```sql
   CREATE TABLE students (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       age INT
   );
   ```

---

### 2. Create Operation (INSERT)

1. In `/src/week3`, create a script `create_student.py`:

   ```python
   import psycopg2

   def create_student(name, age):
       conn = psycopg2.connect(
           dbname="course_project",
           user="postgres",
           password="yourpassword",
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
   ```
2. Run the script.
3. Check in pgAdmin:

   ```sql
   SELECT * FROM students;
   ```

---

### 3. Read Operation (SELECT)

1. Create a script `read_students.py`:

   ```python
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
           dbname="course_project",
           user="postgres",
           password="yourpassword",
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
   ```
2. Run it — you should see a list of `Student` objects.

---

### 4. Update Operation (UPDATE)

1. Create a script `update_student.py`:

   ```python
   import psycopg2

   def update_student_age(student_id, new_age):
       conn = psycopg2.connect(
           dbname="course_project",
           user="postgres",
           password="yourpassword",
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
   ```
2. Verify in pgAdmin:

   ```sql
   SELECT * FROM students WHERE id = 1;
   ```

---

### 5. Delete Operation (DELETE)

1. Create a script `delete_student.py`:

   ```python
   import psycopg2

   def delete_student(student_id):
       conn = psycopg2.connect(
           dbname="course_project",
           user="postgres",
           password="yourpassword",
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
   ```
2. Run it, then verify in pgAdmin.

---

## Deliverables

* Four scripts in `/src/week3/`:

  * `create_student.py`
  * `read_students.py`
  * `update_student.py`
  * `delete_student.py`
* Updated **README.md** that includes:

  * How you tested each CRUD function
  * Example output from your scripts

---

## Reflection (answer in README or LMS)

1. Which CRUD operation did you find most intuitive? Which was hardest?
2. How does mapping rows into objects (like the `Student` class) improve maintainability?
3. Why is `conn.commit()` necessary for **INSERT/UPDATE/DELETE** but not for **SELECT**?
4. How would these scripts change if you were handling **user input** instead of hardcoded values?

---

✅ By the end of this workshop, you will have:

* A working set of scripts that perform full CRUD operations,
* An understanding of how to map DB rows to objects,
* Practical experience committing changes to PostgreSQL securely.
