# Challenge:

# Maria is creating a game for her students to practice logic and quick thinking. She wants a program where the computer chooses a random number between 1 and 100, and the player has to guess what it is.

# Besides ensuring playability, Maria wants the program to handle input errors, preventing the user from providing invalid values, such as letters or numbers outside the allowed range.

# Your task is to create a program that generates a random number between 1 and 100 and allows the user to try to guess the number. The program should inform whether the guess is greater or less than the correct number until the user guesses correctly. If the user enters an invalid value or a number outside the range, a ValueError exception should be thrown.

# Example input:

# Try to guess the number (1-100): 50

# Expected output:

# Congratulations! You guessed the number 37 correctly.

# If the number is below:

# Too low! Try again: 17

# Now, if it's above:

# Too high! Try again: 75

# In case of exception:

# Invalid input: Number out of range! Enter a number between 1 and 100.

# Invalid input: invalid literal for int() with base 10: 'abc12'

import random

# numbers = []
# for i in range(1,101):
#   numbers.append(i)

# guess_number = random.choice(numbers)
# number_input = 0

# try: 
#   while guess_number != number_input:
#     number_input = int(input('Input number: '))
#     if guess_number > number_input: 
#       print(f'Too low! Try again: {number_input}')
#     elif guess_number < number_input:
#       print(f'Too high! Try again: {number_input}')
#   print(f'Right on. You got it! Number: {number_input}')
# except ValueError:
#   print('Error: Invalid Input: invalid literal for int()')
# except: 
#   print("Invalid input: Number out of range! Enter a number between 1 and 100")


guess_number = random.randint(1,100)

number_of_attempts = 0

try: 
  while True:
    number_input = int(input('Input number: '))
    number_of_attempts += 1
    if number_input not in range(1,101):
      raise ValueError('Number out of range')
    
    if guess_number > number_input: 
      print(f'Too low! Try again! Attempt number: {number_of_attempts}')
    elif guess_number < number_input:
      print(f'Too high! Try again! Attempt number: {number_of_attempts}')
    elif guess_number == number_input: 
      print(f'Right on. You got it! Correct number: {number_input}. Number of attempts: {number_of_attempts}')
      break
except ValueError as e: 
  print(f'Error: {e}')