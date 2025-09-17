# Workshop: Environment Setup & PostgreSQL Connection

**Course:** DBAS 3200 – Data-Driven Application Programming
**Week 1 Focus:** Course intro, VS Code environment setup, GitHub repo initialization, PostgreSQL + pgAdmin setup, and testing a database connection.

---

## Learning Outcomes (this workshop supports)

* **Outcome 12:** Establish reliable data connections within an application.
* **Outcome 16:** Demonstrate professionalism in project setup and documentation.

---

## Workshop Activities

### 1. Install & Configure VS Code

1. Download and install **Visual Studio Code** (if not already installed).

   * [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Install the following VS Code extensions:

   * **Python** (if using Python stack)
   * **C# Dev Kit** (if using .NET stack)
   * **SQLTools** + **SQLTools PostgreSQL Driver** (to connect directly to Postgres inside VS Code)
   * **GitHub Pull Requests and Issues** (for repo integration)
   * **Prettier** (for code formatting)
3. Test your environment:

   * Open a new terminal in VS Code.
   * Run `python --version` or `dotnet --version` to confirm your runtime is installed.

---

### 2. Install & Configure PostgreSQL + pgAdmin

1. Download and install **PostgreSQL** (latest stable version) with **pgAdmin 4**:

   * [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
2. During setup, choose a **superuser password** you will remember.
3. Open **pgAdmin 4** → Connect to the default server (`localhost`).
4. Create a new database named:

   ```
   course_project
   ```
5. Verify you can query the database:

   ```sql
   SELECT version();
   ```

---

### 3. Create a GitHub Repository

1. Log in to your GitHub account.
2. Create a new repository named:

   ```
   dbas3200-project
   ```

   * Set visibility to **Private** (recommended).
3. Clone it locally from VS Code:

   * Open Command Palette → `Git: Clone`.
4. Inside the repo, create the following structure:

   ```
   /src
   /migrations
   /docs
   README.md
   ```
5. Commit & push your initial setup:

   ```bash
   git add .
   git commit -m "Initial project setup"
   git push
   ```

---

### 4. Initialize Migration Tool (Starter Setup)

Depending on your language stack:

* **Python + SQLAlchemy + Alembic**

  ```bash
  pip install sqlalchemy psycopg2 alembic
  alembic init migrations
  ```

* **.NET + Entity Framework Core**

  ```bash
  dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL
  dotnet ef migrations add InitialCreate
  dotnet ef database update
  ```

* **Node.js + Sequelize**

  ```bash
  npm install sequelize pg pg-hstore
  npx sequelize-cli init
  ```

📌 *For this week, just ensure migrations folder and configuration exist — we’ll build real models later.*

---

### 5. Lab: Build & Test a Connection String

1. Use your DB credentials to form a connection string.

   **General PostgreSQL format:**

   ```
   postgresql://<username>:<password>@localhost:5432/course_project
   ```

2. Write a short script that connects and runs a test query.

   **Python example (psycopg2):**

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
   cur.execute("SELECT NOW();")
   print("Current time:", cur.fetchone())

   conn.close()
   ```

3. Save this file as `/src/test_connection.py`.

4. Run the script in VS Code terminal:

   ```bash
   python src/test_connection.py
   ```

5. Confirm the output prints the current database time.

6. Commit and push your working code to GitHub.

---

## Deliverables

* Working script that connects to PostgreSQL and prints a timestamp.
* Updated **README.md** containing:

  * IDE + extensions used
  * DB setup method (Postgres + pgAdmin)
  * Steps followed to connect successfully

---

## Reflection (create a reflection text file and add the questions below with answers)

1. What steps went smoothly, and where did you get stuck?
2. How does PostgreSQL + pgAdmin compare to other DB tools you’ve used (if any)?
3. What risks are associated with committing connection strings to GitHub?
4. What habits (repo organization, documentation, testing) from today will help you in professional software projects?

---

At the end of this workshop, you will have:

* A clean repo on GitHub,
* PostgreSQL + pgAdmin running locally,
* A migration tool initialized,
* A working DB connection script you can reuse in future labs.

---
