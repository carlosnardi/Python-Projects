
def addition(number_a, number_b):
  return number_a + number_b

def subtraction(number_a, number_b):
  return number_a - number_b

def multiplication(number_a, number_b):
  return number_a * number_b

def division(number_a, number_b):
  return number_a / number_b

def operator():
  try:
    number_a = int(input('Enter the first number: '))
    operation = input('Choose the operation (+, -, *, /): ')
    number_b = int(input('Enter the second number: '))
    if operation == '+':
      print(f'Result: {addition(number_a, number_b)}')
    elif operation == '-':
      print(f'Result: {subtraction(number_a, number_b)}')
    elif operation == '*':
      print(f'Result: {multiplication(number_a, number_b)}')
    elif operation == '/':
      print(f'Result: {division(number_a, number_b)}')
    else:
      print('Invalid option')
  except ValueError:
    print('Error: Invalid input. Enter only numbers.')
  except ZeroDivisionError:
    print('Error: Division by zero is not allowed')
      