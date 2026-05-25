import sqlite3

DB_NAME = "database/expense_tracker.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # Transactions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        type TEXT NOT NULL,

        category TEXT NOT NULL,

        amount REAL NOT NULL,

        description TEXT,

        date TEXT NOT NULL
    )
    """)

    # Budget Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        monthly_budget REAL
    )
    """)

    conn.commit()

    conn.close()


create_tables()