# .github/workflows/main.yml
name: Django CI

on:
  push:
    branches:
      - main  # Adjust this branch based on your default branch

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          python manage.py test

  lint:
    name: Linting
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Flake8 and Black
        run: |
          python -m pip install flake8 black

      - name: Run Flake8 and Black
        run: |
          flake8 . && black --check --diff .
