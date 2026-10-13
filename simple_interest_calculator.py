"""
Simple Interest Calculator

This program asks a user for their name, principal amount,
interest rate percentage, and time in years. It validates numeric input,
calculates simple interest, and displays the result.

The program demonstrates:
- User input and input validation
- String manipulation
- Exception handling
- Formatted output
"""

def get_positive_number(prompt):
    """Prompt the user until a valid non-negative number is entered."""
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                raise ValueError("The inputed value cannot be negative.")

            return value

        except ValueError as error:
            print(f"Invalid input: {error}")
            print("Please enter a valid positive number.\n")

# Get and clean the user's name
while True:
    name = input("Enter your name: ").strip()

    if name:
        break

    print("Name cannot be empty. Please try again.")

# String transformation: convert the name to title case
formatted_name = name.title()

# String analysis: determine how many words are in the name
name_word_count = len(formatted_name.split())

# Get financial information from the user
principal = get_positive_number("Enter the principal amount: $")
rate = get_positive_number("Enter the interest rate (%): ")
time = get_positive_number("Enter the time in years: ")

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Calculate the total amount
total_amount = principal + simple_interest

# Display results
print("\n--- Simple Interest Results ---")
print(f"Name: {formatted_name}")
print(f"Your name contains {name_word_count} word(s).")
print(f"Principal Amount: ${principal:,.2f}")
print(f"Interest Rate: {rate:.2f}%")
print(f"Time: {time:.2f} year(s)")
print(f"Simple Interest: ${simple_interest:,.2f}")
print(f"Total Amount: ${total_amount:,.2f}")