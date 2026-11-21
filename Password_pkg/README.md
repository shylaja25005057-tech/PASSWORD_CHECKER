
# Advanced Password Strength Checker

## About the Project

The Advanced Password Strength Checker is a Python-based application
that analyses password strength using different conditions.

It provides a detailed report and suggestions to help users understand
password quality.

## Features

1. Password length checking.
2. Uppercase letter detection.
3. Lowercase letter detection.
4. Number detection.
5. Special character detection.
6. Common password detection.
7. Repeated character detection.
8. Sequential pattern detection.
9. Password strength scoring.
10. Estimated entropy calculation.
11. Detailed security feedback.
12. Multiple password checking.
13. Interactive command-line interface.

## Technologies Used

- Python
- Regular Expressions
- Dataclasses
- Math Module
- Unit Testing
- GitHub

## Project Structure

password_pkg/
- __init__.py
- checker.py
- cli.py

tests/
- test_checker.py

pyproject.toml
README.md

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Open the project folder:

cd YOUR_PROJECT_FOLDER

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install the package:

python -m pip install .

## Run the Application

password-check

Alternatively:

python -m password_pkg.cli

## Run Tests

python -m unittest discover -s tests -v

## Scoring System

The application uses a score out of 10.

- Password length: 3 points
- Character variety: 4 points
- Pattern checks: 3 points

## Strength Categories

Strong: Score 9 or above and at least 12 characters.
Moderate: Score 6 or above and at least 8 characters.
Weak: Other passwords.

## Disclaimer

This is an educational password strength estimator.
It does not guarantee password security or check breached-password databases.

The program does not intentionally save or transmit passwords.