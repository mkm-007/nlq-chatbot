# Engineering notes

## Design boundary

Question → validated intent → parameterized SELECT → read-only SQLite → structured answer

This is a constrained parser, not general natural-language understanding. No live LLM, LangChain, PostgreSQL, or Snowflake adapter is implemented. The fixture includes fictional salary records for demonstration; do not connect this demo to private personnel data. Database controls are defense in depth, not a production authorization system.

## Review walkthrough

1. Run `python run_demo.py` and locate the code producing every output field.
2. Run `python -m pytest -q`; change a fixture and explain why its assertion changes.
3. Explain one refusal case and one case the current implementation cannot handle.
4. Trace an input from parsing to the final result, including validation and source/data boundaries.

## Future work (not implemented)

A model-backed extension should have a typed input/output contract, mocked provider tests, explicit opt-in credentials, timeouts, and a measured evaluation set. Treat model output as untrusted. Never send private CATS material to a model. Add infrastructure only when its behavior can be tested and demonstrated; adding a library name alone is not an upgrade.
