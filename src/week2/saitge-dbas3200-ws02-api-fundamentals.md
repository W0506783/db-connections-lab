# Workshop 02: Safe Connections & Querying Data

**Course:** DBAS 3200 – Data-Driven Application Programming
**Week 2 Focus:** Opening/closing database connections, writing parameterized queries, preventing SQL injection, and running a simple read query.

---

## Learning Outcomes (this workshop supports)

* **Outcome 12:** Establish reliable data connections within an application.
* **Outcome 13:** Perform input/output operations with secure queries.
* **Outcome 14:** Implement CRUD operations safely.

---

## Workshop Activities

### 1. Review & Setup

1. Open your `dbas3200` repo in **VS Code**.
2. Confirm that your `/src/test_connection.py` (from Week 1) runs successfully.
3. Create a new folder for this week’s work:

   ```
   /src/week2
   ```

---

### 2. Open & Close Connections (Best Practices)

1. In Python, create a file `open_close.py`:

   ```python
   import psycopg2

   try:
       conn = psycopg2.connect(
           dbname="course_project",
           user="postgres",
           password="yourpassword",
           host="localhost",
           port="5432"
       )
       print("Connection opened successfully!")

   finally:
       if conn:
           conn.close()
           print("Connection closed.")
   ```
2. Run it in VS Code terminal:

   ```bash
   python src/week2/open_close.py
   ```
3. Notice how the `finally` block guarantees the connection closes.

👉 **Professional habit:** Always close connections to avoid leaks.

---

### 3. Parameterized Queries (Safe Input)

1. Create a sample table in **pgAdmin** (or VS Code SQLTools):

   ```sql
   CREATE TABLE students (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       age INT
   );

   INSERT INTO students (name, age)
   VALUES ('Alice', 21), ('Bob', 25), ('Charlie', 22);
   ```
2. Create a Python file `param_query.py`:

   ```python
   import psycopg2

   conn = psycopg2.connect(
       dbname="course_project",
       user="postgres",
       password="yourpassword",
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
   ```
3. Run it and test with inputs like **Alice** or **Charlie**.

---

### 4. SQL Injection Demonstration & Prevention

1. Run the query with a malicious input:

   ```
   Alice' OR '1'='1
   ```

   * If you mistakenly used string concatenation (`"... WHERE name = '" + student_name + "';"`), this would return **all rows** — an SQL injection vulnerability.
   * With parameterized queries (`%s`), the input is treated as data, not code.
2. Write a quick note in your README: *“Parameterized queries protect against SQL injection because the DB driver sends user input separately from the SQL command.”*

---

### 5. Simple Read Query Lab

1. Create a new script `simple_read.py`:

   ```python
   import psycopg2

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
   for row in rows:
       print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

   conn.close()
   ```
2. Run it and verify that it prints the 3 students you inserted.

---

## Deliverables

* **Code:** Three scripts (`open_close.py`, `param_query.py`, `simple_read.py`) in `/src/week2/`.
* **README update:**

  * Steps you used to test parameterized queries.
  * A short explanation of how SQL injection works and why parameterized queries prevent it.
* **GitHub push:** Commit and push your Week 2 code + updated README.

---

## Reflection (answer in README or LMS)

1. Why is it important to close database connections, especially in long-running apps?
2. What risks does SQL injection pose to real-world systems?
3. How do parameterized queries demonstrate professionalism in coding?
4. Which of today’s scripts (open/close, parameterized, or read query) do you think is most important for building reliable applications, and why?

---

✅ At the end of this workshop, you will have:

* Practiced safe connection handling,
* Written your first parameterized query,
* Prevented SQL injection,
* Run a simple **SELECT** query that outputs data from PostgreSQL.