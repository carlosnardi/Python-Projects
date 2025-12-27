# A bank is developing a system for ATMs and needs a program that simulates a cash withdrawal. The ATM must dispense the amount requested by the user using the fewest possible banknotes. The available banknotes are: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, and R$ 2.

# Create a program that asks the user for the withdrawal amount and calculates how many banknotes of each type will be needed to dispense the amount. The program must ensure that the requested amount is valid (a multiple of 2, since there are no R$ 1 banknotes) and handle input errors if a valid numerical value is not entered.

# Example of input:

# Enter the withdrawal amount: 188

# Expected output:

# Bills dispensed:

# 1 of R$ 100
# 1 of R$ 50
# 1 of R$ 20
# 1 of R$ 10
# 1 of R$ 5
# 1 of R$ 2

# If you make a withdrawal of a non-invalid (odd) amount:

# Error: The amount must be a multiple of 2.

withdrawal = int(input('Enter the withdrawal amount: '))

