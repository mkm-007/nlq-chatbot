from nlq_chatbot.db import init_db
from nlq_chatbot.pipeline import answer_question, nl_to_sql


def test_nl_to_sql_count():
    sql = nl_to_sql("How many employees are in Engineering?")
    assert "COUNT" in sql.upper()
    assert "Engineering" in sql


def test_answer_question():
    init_db()
    result = answer_question("How many employees are in Engineering?")
    assert result["answer"] == "2"
    assert "COUNT" in result["sql"].upper()
