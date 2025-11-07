
# Challenge: 

# Create a program that asks the user for a CPF number (Brazilian taxpayer ID) and checks if it has 11 digits and contains only numbers.

# Example input:
# Enter your CPF: 12345678901
# Expected output:
# Valid CPF.
# If invalid:
# Enter your CPF: 1234abc567 Error: The CPF must contain only numbers.
# If the CPF has a number of digits other than 11:
# Enter your CPF: 1234567 Error: The CPF must have exactly 11 digits.

from id_validation.validation import check_id 

print(check_id())