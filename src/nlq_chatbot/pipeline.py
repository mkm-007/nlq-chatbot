"""Constrained offline intent parser. No LLM is invoked."""
import re
from nlq_chatbot.db import run_sql

DEPARTMENTS = {'engineering': 'Engineering', 'hr': 'HR', 'finance': 'Finance'}


def parse_question(question):
    if not isinstance(question, str) or not question.strip() or len(question) > 500:
        raise ValueError('Enter a question between 1 and 500 characters')
    q = question.lower().strip().rstrip('?').strip()
    if re.search(r'\b(drop|delete|update|insert|alter|attach|pragma)\b', q) or ';' in q:
        raise ValueError('Write operations and SQL statements are not allowed')
    patterns = [
        ('count', r'(?:how many employees|count employees)(?: are)?(?: in (engineering|hr|finance))?'),
        ('list', r'list employees(?: in (engineering|hr|finance))?'),
        ('average', r'(?:what is the )?average salary(?: in (engineering|hr|finance))?')]
    for intent, pattern in patterns:
        match = re.fullmatch(pattern, q)
        if match:
            return intent, DEPARTMENTS.get(match.group(1))
    raise ValueError('Unsupported question. Try: List employees in HR; How many employees; Average salary in Finance')


def compile_query(question):
    intent, department = parse_question(question)
    projection = {'count': 'COUNT(*) AS count', 'average': 'AVG(salary) AS avg_salary',
                  'list': 'name, department, salary'}[intent]
    sql = f'SELECT {projection} FROM employees'
    parameters = ()
    if department:
        sql += ' WHERE department = ?'
        parameters = (department,)
    if intent == 'list':
        sql += ' ORDER BY name LIMIT 100'
    return sql, parameters


def nl_to_sql(question):
    return compile_query(question)[0]


def answer_question(question, path=None):
    sql, parameters = compile_query(question)
    rows = run_sql(sql, parameters, path)
    if len(rows) == 1 and len(rows[0]) == 1:
        answer = str(next(iter(rows[0].values())))
    else:
        answer = '; '.join(', '.join(f'{k}={v}' for k, v in row.items()) for row in rows) or 'No rows'
    return {'mode': 'deterministic', 'sql': sql, 'parameters': list(parameters), 'rows': rows, 'answer': answer}
