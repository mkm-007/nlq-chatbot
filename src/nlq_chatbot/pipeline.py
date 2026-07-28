"""NL → SQL pipeline.

Uses a deterministic router for offline demos. Swap `llm_complete` for
LangChain + real LLM in extensions/ when a JD needs live LLM consumption.
"""
from __future__ import annotations

import re

from nlq_chatbot.db import run_sql


def llm_complete(prompt: str) -> str:
    """Placeholder LLM call — replace with LangChain ChatModel in extensions."""
    _ = prompt
    return ""


def nl_to_sql(question: str) -> str:
    q = question.lower()
    if "how many" in q and "engineering" in q:
        return (
            "SELECT COUNT(*) AS count FROM employees "
            "WHERE department = 'Engineering'"
        )
    if "list" in q and "hr" in q:
        return "SELECT name, department, salary FROM employees WHERE department = 'HR'"
    if "average" in q and "engineering" in q:
        return (
            "SELECT AVG(salary) AS avg_salary FROM employees "
            "WHERE department = 'Engineering'"
        )
    # Fallback: refuse unsafe free-form SQL
    if re.search(r"\b(drop|delete|update|insert)\b", q):
        raise ValueError("Write operations are not allowed")
    return "SELECT name, department FROM employees LIMIT 5"


def answer_question(question: str) -> dict:
    sql = nl_to_sql(question)
    rows = run_sql(sql)
    if len(rows) == 1 and len(rows[0]) == 1:
        value = next(iter(rows[0].values()))
        answer = str(value)
    else:
        answer = "; ".join(
            ", ".join(f"{k}={v}" for k, v in row.items()) for row in rows
        ) or "No rows"
    return {"sql": sql, "rows": rows, "answer": answer}
