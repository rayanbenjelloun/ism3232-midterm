# Terminal Record: [Ridgeline Tool Rental]

## 1. Building the project 
```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git init
pwd
python3 -m venv .venv
source .venv/bin/activate 
which python3
pip list
pip install pytest ruff
pip list
pip freeze > requirements.txt
cat requirements.txt 
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
cat .gitignore
touch business_rules.py main.py
mkdir -p tests
touch tests/__init__.py tests/test_business_rules.py
touch commands.md README.md
git add .gitignore requirements.txt main.py tests/__init__.py
git commit -m 'midterm: set up project structure and dependencies'
git log --oneline
git remote add origin https://github.com/rayanbenjelloun/ism3232-midterm.git 
git branch -M main
ruff format .
ruff check .
pytest -v
git push -u origin main
```
## 2. The virtual environment
```
which python3
```

```
/home/rayanbenjeloun/ism3232-midterm/.venv/bin/python3
```
the path points to the python inside the folder showing that the virtual environment is active 
## 3. The project structure
```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
the __pycache__ folder is in my computer but not my github because it is listed in .gitignore
## 4. Every function and test
```
rg 'def '
```

```
business_rules.py
16:def calculate_rental_cost(daily_rate: float, days: int) -> float:
21:def get_rental_discount(days: int, contractor: bool = False) -> float:
31:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
42:def requires_deposit(quote: float) -> bool:
47:def needs_inspection(days: int, quote: float) -> bool:
52:def total_quoted(rentals: list) -> float:
64:def largest_rental(rentals: list) -> str:
84:def format_rental_line(

tests/test_business_rules.py
13:def test_calculate_rental_cost():
17:def test_rental_discount_below_three_days():
21:def test_rental_discount_at_three_days():
25:def test_rental_discount_at_six_days():
29:def test_rental_discount_at_seven_days():
33:def test_rental_discount_contractor_two_days():
37:def test_rental_discount_contractor_seven_days():
41:def test_quote_adds_damage_waiver():
45:def test_quote_at_damage_waiver_limit():
49:def test_quote_one_cent_below_damage_waiver_limit():
53:def test_quote_applies_ten_percent_discount():
57:def test_quote_applies_twenty_percent_discount():
61:def test_quote_contractor_discount_before_damage_waiver():
65:def test_deposit_below_limit():
69:def test_deposit_at_limit():
73:def test_deposit_above_limit():
77:def test_inspection_below_required_days():
81:def test_inspection_at_required_days():
85:def test_inspection_at_quote_limit():
89:def test_inspection_below_quote_limit():
93:def test_total_quoted_empty():
97:def test_total_quoted_one_rental():
104:def test_total_quoted_multiple_rentals():
113:def test_largest_rental_empty():
117:def test_largest_rental_finds_largest_quote():
141:def test_largest_rental_tie_keeps_first():
159:def test_format_rental_line_no_deposit_no_inspection():
164:def test_format_rental_line_deposit_and_inspection():
169:def test_format_rental_line_inspection_only():
174:def test_format_rental_line_deposit_only():
```
business_rules.py defines 8 functions and tests/test_business_rules.py defines 30 tests.
## 5. Which files print
```
rg -l 'print'
```

```
commands.md
main.py
```
commands.md and main.py, main prints the report and commands matches since it contains the word print, business_rules.py doesn't print because it contains no print() calls.
## 6. The commit history
```
git log --oneline
```

```
75694bc (HEAD -> main, origin/main) midterm: add rental report and summary calculations
2025e06 midterm: add rental line formatting and four tests
37f64ed midterm: add largest rental function and three tests
7939383 midterm: add total quoted function and three tests
246d44d midterm: add deposit and inspection rules with seven tests
d6f2207 midterm: add quote calculations and sixt tests
c96a054 midterm: add rental cost and discount functions with seven tests
293a7ee midterm: set up project structure and dependencies
```
There were 8 commits at that point.