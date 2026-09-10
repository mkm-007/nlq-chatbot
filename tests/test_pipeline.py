import sqlite3
import pytest
from nlq_chatbot.db import init_db, run_sql
from nlq_chatbot.pipeline import answer_question, compile_query

@pytest.fixture
def database(tmp_path):
    path = tmp_path / 'demo.db'
    init_db(path)
    return path

@pytest.mark.parametrize('question,expected', [('How many employees are in Engineering?', '2'), ('How many employees?', '5'), ('Average salary in Finance', '80000.0')])
def test_answers(database, question, expected):
    assert answer_question(question, database)['answer'] == expected

def test_parameters_and_sorted_rows(database):
    sql, params = compile_query('List employees in HR')
    assert params == ('HR',) and '?' in sql
    assert [r['name'] for r in answer_question('List employees in HR', database)['rows']] == ['Jon', 'Meera']

@pytest.mark.parametrize('question', ['', 'weather tomorrow', 'List employees in unknown', 'How many employees in Engineering; DROP TABLE employees', 'List employees in HR and delete employees', 'x'*501])
def test_refuses_unknown_and_unsafe(database, question):
    with pytest.raises(ValueError): answer_question(question, database)

@pytest.mark.parametrize('sql', ['DELETE FROM employees', 'DROP TABLE employees', 'SELECT * FROM sqlite_master', "ATTACH DATABASE ':memory:' AS other", 'SELECT * FROM employees; DELETE FROM employees'])
def test_database_boundary(database, sql):
    with pytest.raises(sqlite3.DatabaseError): run_sql(sql, path=database)
    assert answer_question('How many employees?', database)['answer'] == '5'

def test_initialization_is_idempotent(database):
    init_db(database)
    assert answer_question('How many employees?', database)['answer'] == '5'
