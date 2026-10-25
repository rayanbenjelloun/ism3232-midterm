# ISM3232 Midterm: [Ridgeline Tool Rental]

- **Name:** [Rayan Benjelloun]
- **Version:** [ALPHA]
- **Date:** [10/25/2026]

## What This Program Does
This program calculates quotes for eight equipment rentals. It applies discounts, damage waivers,then it checks whether or not each rental needs a deposit or an inspection. The report shows each customer's quote and the rental summary.
## Business Rules
1. Calculate the starting rental cost by multiplying the daily rate and the number of rental days. 
2. Apply no standard discount for less than 3 days, apply 10% discount for 3-6 days, apply 20% discount for 7 or more days.
3. Give licensed contractors at least a 10% discount even for rentals less than 3 days.
4. Add a $25 damage waiver when the cost after discounts is less than $150.
5. Require a deposit when the quote is $1,000 or more.
6. Require a pickup inspection when the rental lasts at least 5 days and the final quote is more than $800.
## How to Run
```
python3 -m .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
## How to Test
```
ruff format --check
ruff check .
pytest -v
```
I wrote 30 tests.
## Files in This Repository
business_rules.py: contains the eight business functions and named constants.
main.py: contains the rental data and prints the rental report and summary.
commands.md: Records the terminal commands, their outputs, and explanations.
READ.md: Explains the project, business rules, setup and testing.
requirements.txt: Lists the python dependencies and their versions.
.gitignore: keeps the virtual environment and python cache files out of Git.
tests/__init__.py: Marks the tests folder as a python package.
tests/test_business_rules.py: contains the 30 tests for the business functions.
## AI Use Statement
I did not use ai to complete this midterm.