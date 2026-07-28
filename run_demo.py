"""NLQ chatbot demo: natural language → SQL → answer (offline-safe)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from nlq_chatbot.db import init_db
from nlq_chatbot.pipeline import answer_question


def main() -> None:
    init_db()
    questions = [
        "How many employees are in Engineering?",
        "List employees in HR",
        "What is the average salary in Engineering?",
    ]
    for q in questions:
        result = answer_question(q)
        print(f"Q: {q}")
        print(f"SQL: {result['sql']}")
        print(f"A: {result['answer']}")
        print("---")


if __name__ == "__main__":
    main()
