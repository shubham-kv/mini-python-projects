import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path.home() / ".todos_cli.db.sqlite3"


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print("SQLite Error:", e)
        raise
    finally:
        conn.close()


def init_db():
    create_todos_table_query = """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_done INTEGER NOT NULL CHECK (is_done IN (0, 1))
        )
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(create_todos_table_query)


def add_todo(name: str) -> int:
    insert_todo_query = """
        INSERT INTO todos(name, is_done)
        VALUES (?, ?)
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur = cur.execute(insert_todo_query, (name, False))
        return cur.rowcount


def update_todo_name(id: int, new_name: str) -> int:
    update_todo_query = """
        UPDATE todos
        SET name = ?
        WHERE id = ?
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur = cur.execute(update_todo_query, (new_name, id))
        return cur.rowcount


def update_todo_is_done(id: int, is_done: bool) -> int:
    update_todo_query = """
        UPDATE todos
        SET is_done = ?
        WHERE id = ?
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur = cur.execute(update_todo_query, (is_done, id))
        return cur.rowcount


def get_todos():
    select_todos_query = """
        SELECT * FROM todos
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(select_todos_query)

        todos: list[dict[str, int | str]] = []

        for row in cur.fetchall():
            todos.append(
                {"id": row["id"], "name": row["name"], "is_done": row["is_done"]}
            )
        return todos


def delete_todo(id: int) -> int:
    delete_todo_query = """
        DELETE FROM todos
        WHERE id = ?
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur = cur.execute(delete_todo_query, (id,))
        return cur.rowcount
