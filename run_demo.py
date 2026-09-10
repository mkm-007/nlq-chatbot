"""Query the synthetic fixture; supply --question for your own supported input."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))
from nlq_chatbot.db import init_db
from nlq_chatbot.pipeline import answer_question

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--question', default='How many employees are in Engineering?')
    args = parser.parse_args()
    init_db()
    try:
        print(json.dumps(answer_question(args.question), indent=2))
    except ValueError as exc:
        print(json.dumps({'status': 'refused', 'error': str(exc)}))
        return 2
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
