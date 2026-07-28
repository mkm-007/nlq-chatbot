from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine, text

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "demo.db"
ENGINE = create_engine(f"sqlite:///{DB_PATH}", future=True)


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with ENGINE.begin() as conn:
        conn.execute(
            text(
                """
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    salary REAL NOT NULL
                )
                """
            )
        )
        count = conn.execute(text("SELECT COUNT(*) FROM employees")).scalar()
        if count == 0:
            conn.execute(
                text(
                    """
                    INSERT INTO employees (name, department, salary) VALUES
                    ('Asha', 'Engineering', 90000),
                    ('Ravi', 'Engineering', 85000),
                    ('Meera', 'HR', 70000),
                    ('Jon', 'HR', 72000),
                    ('Priya', 'Finance', 80000)
                    """
                )
            )


def run_sql(sql: str) -> list[dict]:
    with ENGINE.connect() as conn:
        rows = conn.execute(text(sql)).mappings().all()
        return [dict(r) for r in rows]
