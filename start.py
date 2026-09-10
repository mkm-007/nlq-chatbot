"""Interactive local demo. Run with Python 3.11 or newer; no dependencies."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))

from nlq_chatbot.db import init_db
from nlq_chatbot.pipeline import answer_question

def main():
    init_db()
    print('Employee database demo (fictional records)')
    print('Try: How many employees are in Engineering?')
    print('Or: List employees in HR | Average salary in Finance')
    print('Type quit to exit. No internet connection is used.\n')
    while True:
        try:
            question = input('Question> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye.'); return
        if question.lower() in {'quit', 'exit'}:
            print('Goodbye.'); return
        if not question:
            continue
        try:
            result = answer_question(question)
            print('Answer:', result['answer'])
            print('SQL:', result['sql'])
            print('Parameters:', result['parameters'], '\n')
        except ValueError as exc:
            print(str(exc), '\n')

if __name__ == '__main__':
    main()
