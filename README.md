# NLQ Chatbot over Database

Natural-language-to-SQL chatbot for staff who need answers from operational records without writing SQL. Answers are grounded on database results.

**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python · LangChain-style pipeline · SQLite (local) / Postgres-ready · LLM interface (mockable offline)

---

## Problem

Staff needed answers from operational records but could not write SQL. Answers had to come from the database — not from model guesses.

## What it does

1. Map natural-language questions to a constrained SQL path  
2. Execute against a demo employee schema  
3. Return answers grounded on query results  

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

Demo output: [`demo_output.txt`](./demo_output.txt)

## Design notes

- Offline-mockable LLM interface so demos stay reproducible without API keys  
- Local SQLite for instant proof; Postgres-ready path for staff handoff realism  
- Prefer constrained query mapping over free-form SQL generation for safer staff use  

## Layout

```
src/nlq_chatbot/
tests/
extensions/
run_demo.py
demo_output.txt
```

## Portfolio

[mkm-007/MKM](https://github.com/mkm-007/MKM) · [Live site](https://mkm-007.github.io/MKM/)
