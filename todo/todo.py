import sqlite3
import argparse
import os


DB_NAME = os.path.join(os.path.expanduser("~"), ".todo_app.db")


def init_db(func):
    def wrapper(*args, **kwargs):
        try:
            # Try running the decorated function
            return func(*args, **kwargs)
        except sqlite3.OperationalError:
            # Create the todos table if it doesn't exist
            create_todo_table()

            # Try running the decorated function again
            return func(*args, **kwargs)

    return wrapper


def display(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        show_todos()
        return result

    return wrapper


def create_todo_table():
    """Create the todo table in the database if it doesn't already exist."""
    print("table doesn't exist. creating...")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT, completed INTEGER)"
    )

    conn.commit()
    conn.close()

    print("table todos created.")


@display
@init_db
def add_todo(task: str):
    """Add a new todo to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO todos (task, completed) VALUES (?, 0)", (task,))

    conn.commit()
    conn.close()


@display
@init_db
def delete_todo(task_id: int):
    """Delete a todo from the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("DELETE FROM todos WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()


def delete_all_todos():
    """Delete a todo from the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    prompt = input("press Y to confirm, any other key to cancel")
    if prompt == "Y":
        c.execute("DELETE FROM todos")
        conn.commit()
        conn.close()
    else:
        print("Cancelled")


@display
@init_db
def mark_todo_complete(task_id: int):
    """Mark a todo as completed in the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("UPDATE todos SET completed = 1 WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()


def show_todos():
    """Retrieve all todos from the database and print them to the terminal."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM todos")
    todos = c.fetchall()

    for todo in todos:
        completed = "✔" if todo[2] else " "
        print(f"{todo[0]}. [{completed}] {todo[1]}")

    if not todos:
        print("Nothing to show. Add a todo now.")

    conn.close()


@display
@init_db
def mark_todo_uncomplete(task_id: int):
    """Mark a todo as uncomplete in the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("UPDATE todos SET completed = 0 WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()
