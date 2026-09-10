# NLQ Chatbot over Database

Ask questions about a small employee database without writing SQL. The result includes the answer, the SQL query, and its parameters so you can see exactly where the answer came from.

## Run it on your computer

You need **Python 3.11 or newer**. Check with `python3 --version` on macOS/Linux or `py -3 --version` on Windows. If Python is missing, install it from [python.org](https://www.python.org/downloads/) and reopen your terminal.

### 1. Download the project

If you have Git, run:

```bash
git clone https://github.com/mkm-007/nlq-chatbot.git
cd nlq-chatbot
```

Without Git: select **Code → Download ZIP** on this GitHub page, extract the ZIP, and open a terminal in the extracted folder. You should see `README.md`, `start.py`, and `run_demo.py` in that folder. Open the folder in VS Code and choose **Terminal → New Terminal** if that is easier.

### 2. Start the interactive demo

**macOS / Linux:**

```bash
python3 start.py
```

**Windows PowerShell:**

```powershell
py -3 start.py
```

No package installation, API key, database account, or paid service is needed for this step. This is a terminal program: type your question/request at its prompt and press Enter. Type `quit` to stop, or press Ctrl+C.

Try this first:

```text
How many employees are in Engineering?
```

The answer is **2**. Listing HR employees returns **Jon** and **Meera**; the average salary in Finance is **80000.0**. These are fictional sample records.

### 3. Run a single request

For scripts or a structured JSON response, use:

```bash
python3 run_demo.py --question "How many employees are in Engineering?"
```

On Windows, replace `python3` with `py -3`. See [sample output](demo_output.txt) for a complete response. These commands finish after one request; `start.py` stays open for more.

## Questions to try

```text
How many employees are in Engineering?
List employees in HR
Average salary in Finance
How many employees?
```

Engineering, HR, and Finance are the supported departments. Omit the department to query all five records. Questions outside the supported patterns return an explanation instead of a guessed answer.

## What happens when you run it

1. The program creates `data/demo.db` and adds five fictional employees on its first run.
2. The parser recognizes a count, list, or average-salary request.
3. It builds a parameterized query and executes it through a read-only connection.
4. It returns the rows and a readable answer. The database remains available between runs.

No database server or account setup is required. The demo creates only its own local SQLite file. `src/nlq_chatbot/db.py` contains the fixture and execution controls; `pipeline.py` handles questions and answers.

## Current scope

This version uses fixed question patterns and SQLite. It does not call an LLM or connect to PostgreSQL/Snowflake. It supports one sample schema, caps returned rows, and rejects writes. It is a local learning project, without user accounts or production access controls.

## Run the tests (optional)

The demos use Python's standard library. **pytest is needed only for tests.** From the repository folder:

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest -q
```

The commands use the environment's Python directly, so you do not need to activate it or change PowerShell's execution policy. GitHub also runs the tests automatically.

## Troubleshooting

- **`python3` or `py` not found**: install Python, reopen your terminal, and check its version.
- **“Can't open file start.py”**: your terminal is in the wrong folder. Open the folder containing this README and `start.py`.
- **A download/install command fails**: downloading the ZIP, cloning, and installing test/compiler dependencies require internet. The Python demo runs offline once downloaded.
- **“Unsupported question”**: copy one of the examples above. Department names outside the sample data are not supported.
- **Database cannot be opened**: keep the downloaded project in a folder you can write to. The program creates its own `data` directory.

## About this project

A personal implementation inspired by my hands-on project experience at CATS, GITAM University. It uses sample data and does not include the original CATS source code.

[Implementation notes](ENGINEERING.md) · [GitHub portfolio](https://github.com/mkm-007/MKM)
