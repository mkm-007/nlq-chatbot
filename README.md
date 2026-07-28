# NLQ Chatbot over Database

Natural-language-to-SQL chatbot so non-technical users can query relational records without writing SQL. Answers are grounded on database results.

**Origin:** Centre for Advanced Technology Solutions, GITAM University (May 2024 – Dec 2024)  
**Stack:** Python · LangChain-style pipeline · SQLite (local) / Postgres-ready · LLM interface (mockable offline)

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## What it does

1. Parse a natural-language question
2. Map to a safe SQL query against a demo employee schema
3. Execute and return a grounded answer

See [`demo_output.txt`](./demo_output.txt) for a captured run.

## Layout

```
src/nlq_chatbot/   # schema, NLQ pipeline, db
tests/
extensions/        # JD-specific modules (Snowflake, RAG hooks, …)
run_demo.py
demo_output.txt
```

## Resume anchor

Built natural-language-to-SQL chatbot so staff can query records without raw SQL; grounded answers on DB results. Designed safe query path and demo workflow for staff-facing use.

## License

Personal portfolio / educational use.
