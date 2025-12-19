# Carlos is creating a simple calculator, but he wants to ensure the program doesn't crash if the user enters invalid values; he needs to handle errors.

# Create a calculator that allows the user to choose between addition, subtraction, multiplication, and division. In addition to modularizing the code into functions, use try-except to handle invalid input errors, which consist of:

# If a character is entered instead of a number | exception to be thrown: ValueError;

# If you try to divide by 0 | exception to be thrown: ZeroDivisionError.

# Example input:

# Enter the first number: 5
# Choose the operation (+, -, *, /): +
# Enter the second number: 7

# Expected output:

# Result: 12

# If none of the listed operations are selected:

# Invalid option

# If a character is entered instead of a number:

# Error: Invalid input. Enter only numbers.

# If you try to divide by 0:

# Error: Division by zero is not allowed.

from calculator_app.operations import operator

operator()