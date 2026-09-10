"""Synthetic SQLite fixture with a separate read-only query connection."""
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[2] / 'data' / 'demo.db'


def init_db(path=None):
    path = Path(path or DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, department TEXT NOT NULL, salary REAL NOT NULL)')
        if conn.execute('SELECT COUNT(*) FROM employees').fetchone()[0] == 0:
            conn.executemany('INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)', [
                ('Asha', 'Engineering', 90000), ('Ravi', 'Engineering', 85000),
                ('Meera', 'HR', 70000), ('Jon', 'HR', 72000), ('Priya', 'Finance', 80000)])


def run_sql(sql, parameters=(), path=None):
    """Read only, one statement, restricted table access, bounded result size."""
    path = Path(path or DB_PATH).resolve()
    conn = sqlite3.connect(path.as_uri() + '?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_FUNCTION}
    def authorize(action, arg1, arg2, database, trigger):
        if action in allowed or (action == sqlite3.SQLITE_READ and arg1 == 'employees'):
            return sqlite3.SQLITE_OK
        return sqlite3.SQLITE_DENY
    conn.set_authorizer(authorize)
    steps = 0
    def budget():
        nonlocal steps
        steps += 1
        return int(steps > 100)
    conn.set_progress_handler(budget, 1000)
    try:
        return [dict(row) for row in conn.execute(sql, parameters).fetchmany(100)]
    finally:
        conn.close()
