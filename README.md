# Temperature Data Generator

This project generates synthetic hourly temperature data using NumPy and pandas.

## Task 1: Generate Synthetic Temperature Data

**Objective:**  
Generate synthetic temperature data

**Requirements:**

- Using NumPy, generate hourly temperature measurements for 5 days.
- Assume temperatures are centered around 20°C
- Allow random variation of about ±5°C
- You should produce 120 temperature values (5 days × 24 hours).

**Project Setup:**

- Create a new Python 3.14 project with Pipenv
- Add pandas, numpy
- Use NumPy to generate arrays, simulate data, work with random numbers
- Use pandas to build DataFrames, work with datetime data, create new columns, groupby and aggregation functions, compute differences between rows

## Task 2: Extend with Testing

**Objective:**  
Extend above synthetic data generator to add pytest to check if the generator functions are returning the correct 1. shape and 2. boundaries. We do not need to test the mock data that is generated, we will be testing the functions itself so that they will never return wrong data.

**Requirements:**

- Put tests in a separate tests dir
- Update code to take input date and starting temperature, validate for wrong input, check if validations work with tests
- Test shape of output
- Test boundaries with parameterization

## Usage

### Prerequisites

- Python 3.14
- Pipenv

### Installation

```bash
pipenv install
```

### Running the Generator

To generate temperature data:

```bash
pipenv run python generator.py
```

### Running Tests

To run the tests:

```bash
pipenv run pytest
```
