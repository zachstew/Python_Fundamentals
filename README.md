# Python Fundamentals

This repository contains a Python program that demonstrates basic Python concepts such as user input, string manipulation, input validation, and exception handling.

## Program Included

### Simple Interest Calculator

The `simple_interest_calculator.py` program asks the user to enter:

- Principal amount
- Interest rate
- Time in years

It calculates simple interest using:

Simple Interest = (Principal × Rate × Time) / 100

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

python simple_interest_calculator.py

## Assumptions

- The interest rate is entered as a percentage.
- For example, 5% should be entered as `5`.
- Negative values are not allowed.

## Testing

I tested the program using valid and invalid inputs.

One edge case I tested was entering text instead of a number. The program displayed an error message and asked the user to enter a valid number.

I also tested a negative number, and the program rejected it and asked the user to try again.
