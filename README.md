🧪 QA Todo Automation Project

This project is a QA Automation framework built with Pytest + Playwright to test a real Todo web application.

It demonstrates:

UI Automation

Page Object Model (POM)

Smoke & Regression test separation

HTML reporting

The tested application:
👉 https://todomvc.com/examples/react/dist/

📁 Project Structure
qa-todo-automation/
│
├── tests/ # Test cases
│ └── test_todo.py
│
├── pages/ # Page Object Model
│ └── todo_page.py
│
├── conftest.py # Pytest fixtures
├── pytest.ini # Markers (smoke, regression)
├── requirements.txt
├── Makefile
└── README.md

🧩 Technologies Used

Python

Pytest

Playwright

Page Object Model

HTML Test Reports

## ✅ What this project proves

- I can build a maintainable UI automation framework using **POM**
- I can organize tests using **pytest markers** (smoke/regression)
- I can generate and share **HTML reports**
- I can run tests via **Makefile commands**

🧪 Test Types
Smoke Tests

Quick checks to verify the main functionality:

User can add a new todo task

Regression Tests

Full test suite to verify:

Adding multiple tasks

Completing a task

Deleting a task

▶️ How to Run
1️⃣ Install dependencies
python -m pip install -r requirements.txt
python -m playwright install

2️⃣ Run Smoke Tests
pytest -v -m smoke

or

make smoke

3️⃣ Run Regression Tests
pytest -v -m regression

or

make regression

4️⃣ Generate HTML Report
pytest -v --html=report.html --self-contained-html

Open report.html in a browser to see detailed results.

🧠 QA Concepts Demonstrated

Page Object Model for maintainable UI automation

Markers (smoke, regression) for test grouping

Fixtures for browser and test setup

Assertions to validate application behavior

## ⚠️ Notes

The demo app used for testing is a public sample (TodoMVC). Test expectations are aligned with the demo behavior.

👩‍💻 Author

Semra K.
Junior QA Automation Engineer
Python • Pytest • Playwright • UI Automation
