# NLQ Chatbot over Database

**Resume project · SPT work unit**  
**Capability:** grounded natural-language access to relational data for non-technical staff  
**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python · LangChain-style pipeline · SQLite (local) / Postgres-ready · LLM interface (mockable offline)

---

## Problem

Staff needed answers from operational records but could not write SQL. Answers had to come from the database — not from model guesses.

## What I built

1. Map natural-language questions to a constrained SQL path  
2. Execute against a demo employee schema  
3. Return answers grounded on query results  

Resume anchor: *Built natural-language-to-SQL chatbot so staff can query records without raw SQL; grounded answers on DB results. Designed safe query path and demo workflow for staff-facing use.*

## SPT bar (junior standard)

| Step | Artifact |
|------|----------|
| Build | `src/nlq_chatbot/` |
| Verify | `python -m pytest -q` |
| Demo | `python run_demo.py` · [`demo_output.txt`](./demo_output.txt) |
| Document | this README |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## Design notes

- Offline-mockable LLM interface so demos stay reproducible without API keys  
- Local SQLite for instant proof; Postgres-ready path for staff handoff realism  
- Prefer constrained query mapping over free-form SQL generation for safer staff use  

## Layout

```
src/nlq_chatbot/
tests/
extensions/        # JD-specific modules (Snowflake, RAG hooks, …)
run_demo.py
demo_output.txt
```

## Portfolio

Full Experience · Projects · SPT → [mkm-007/MKM](https://github.com/mkm-007/MKM)
