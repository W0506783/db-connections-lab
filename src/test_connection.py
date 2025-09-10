import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        # Replace with your actual connection string
        connection = psycopg2.connect(
            "postgresql://lab_user:password@localhost:5432/lab_db"
        )
        print("Connection to PostgreSQL DB successful")
        connection.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    test_connection()
