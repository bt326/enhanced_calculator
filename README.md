# Enhanced Calculator
# Enhanced Calculator 

A professional, test-driven, command-line calculator built in Python using multiple design patterns, pandas-based history management, and full CI/CD automation.

This project demonstrates industry-level practices including modular design, automated testing, configuration management, and 100% test coverage enforcement.

---

##  Features

* Interactive REPL (Read–Eval–Print Loop)
* Advanced operations: add, subtract, multiply, divide, power, root
* Undo / Redo support (Memento Pattern)
* Calculation history using pandas
* Auto-save and load history (CSV)
* Environment-based configuration
* Robust error handling
* Fully tested with pytest (100% coverage)
* GitHub Actions CI pipeline

---

## Design Patterns Used

| Pattern  | Purpose              | File                    |
| -------- | -------------------- | ----------------------- |
| Strategy | Operation execution  | `operations.py`         |
| Factory  | Create operations    | `calculation.py`        |
| Observer | Track history        | `calculator_memento.py` |
| Memento  | Undo/Redo            | `calculator_memento.py` |
| Facade   | Simplified interface | `calculator_repl.py`    |

---

## 📁 Project Structure

```
enhanced_calculator/
│
├── app/
│   ├── calculator_repl.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
│
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_calculator_repl.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   └── test_operations.py
│
├── .env
├── .coveragerc
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/bt326/enhanced_calculator.git
cd enhanced_calculator
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install pytest pytest-cov pandas python-dotenv coverage
```

---

### 4. Configure Environment

Create `.env` file in root directory:

```env
HISTORY_FILE=history.csv
AUTO_SAVE=true
```

---

## ▶ Run the Application

From project root:

```bash
python -m app.calculator_repl
```

---

## Available Commands

| Command      | Description         |
| ------------ | ------------------- |
| add a b      | Addition            |
| subtract a b | Subtraction         |
| multiply a b | Multiplication      |
| divide a b   | Division            |
| power a b    | Power               |
| root a b     | Root                |
| history      | Show history        |
| undo         | Undo last operation |
| redo         | Redo last operation |
| clear        | Clear history       |
| save         | Save history        |
| load         | Load history        |
| help         | Show help           |
| exit         | Exit app            |

Example:

```
>>> add 5 6
Result = 11
```

---

##  Run Tests

Run all tests:

```bash
pytest
```

---

### Run With Coverage

```bash
pytest --cov=app
coverage report
```

Expected:

```
TOTAL 100%
```

---

## Continuous Integration (CI)

This project uses GitHub Actions to:

* Run tests automatically
* Enforce 100% coverage
* Block failing builds

Workflow file:

```
.github/workflows/python-app.yml
```

---

##  Coverage Configuration

Coverage exclusions are handled via:

```
.coveragerc
```

Interactive CLI code is excluded from coverage metrics.

---

##  Error Handling

* Custom exceptions
* LBYL & EAFP patterns
* Input validation
* Division-by-zero handling

---
---

## Acknowledgements

Developed as part of an advanced Python programming and software engineering assignment.

Demonstrates professional-level practices in testing, design patterns, and automation.
