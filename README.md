# NLQ Chatbot over Database

Ask supported questions about synthetic employee records and inspect the SQL, parameters, rows, and answer.

> **Independent portfolio reconstruction.** Inspired by project categories I worked on while gaining practical experience at CATS, GITAM. I do not have access to the original CATS codebases. This repository was created later with AI coding assistance (Cursor/Codex), uses demonstration inputs, and is not original institutional code or evidence of a production deployment. Features and tests below describe this reconstruction only.

## Try it

Python 3.11+; the runtime uses only Python's standard library. No API keys or paid services are needed.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
python run_demo.py --question "Average salary in Finance"
```

The checked-in [demo output](demo_output.txt) is generated from the current implementation. Tests run automatically on pushes and pull requests.

## Architecture

```text
Question → validated intent → parameterized SELECT → read-only SQLite → structured answer
```

## Implemented

- Count, list, and average-salary queries for Engineering, HR, Finance, or all employees.
- Explicit rejection of unknown questions rather than an unrelated fallback answer.
- Parameter binding, read-only database access, table authorization, row cap, and execution budget.
- Isolated temporary databases in tests; repeatable synthetic seed data.

## Scope and limitations

This is a constrained parser, not general natural-language understanding. No live LLM, LangChain, PostgreSQL, or Snowflake adapter is implemented. The fixture includes fictional salary records for demonstration; do not connect this demo to private personnel data. Database controls are defense in depth, not a production authorization system.

## Verification

`tests/` covers successful requests and failure cases. Read the tests alongside the source; test counts are evidence of exercised cases, not a claim of production readiness. [Engineering notes](ENGINEERING.md) explain boundaries and review prompts.

## Background and attribution

The historical CATS work involved Angular, Python, LLM consumption, database querying, document retrieval, and agent-oriented UI workflows, as described by the portfolio owner. Those historical technologies are not automatically dependencies or implemented capabilities here. Public reconstruction work must be described separately from institutional experience in resumes and interviews. Do not backdate these commits or claim institutional adoption.

AI tools assisted implementation. The portfolio owner should run the demo, inspect the code, and be able to explain its decisions and limitations before presenting it as personal proficiency. No confidential CATS code, data, or documents are included.

[Portfolio](https://github.com/mkm-007/MKM)
