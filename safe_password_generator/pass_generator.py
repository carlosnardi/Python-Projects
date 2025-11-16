import os
import random

def initial_screen():
  os.system('clear')
  print('''Safe Pass Gen     
\nSafe Pass Generator App\n''')

def random_alpha():
  alpha = 'a b c d e f g h i j k l m n o p q r s t u v x y z'
  alpha_list_lower = alpha.split(' ')
  appha_list_upper = alpha.upper().split(' ')
  return random.choice(alpha_list_lower), random.choice(appha_list_upper)

def random_number():
  number = '0 1 2 3 4 5 6 7 8 9'
  number_list = number.split(' ')
  return random.choice(number_list)

def random_character():
  character = '# @ % & * ! _ - + = / ?'
  character_list = character.split(' ')
  return random.choice(character_list)

def create_pass():
  num_of_digits = int(input("What is the length of the password to be generated: "))
  password = ''
  options = [random_alpha()[0], random_alpha()[1], random_number(), random_character()]
  first_options = sorted(options)
  for item1 in first_options:
    password += item1
  while len(password) < num_of_digits:
    options = [random_alpha()[0], random_alpha()[1], random_number(), random_character()]
    item2 = random.choice(options)
    password += item2
  return password
    
  
  # Simpler and more fluid alternative:

def create_password():
  capital = 'abcdefghijklmnopqrstuvxyz'
  lowercase = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
  numbers = '0123456789'
  special_char = '#@%&*!_-+=/?'

  password = [
    random.choice(capital), 
    random.choice(lowercase),
    random.choice(numbers),
    random.choice(special_char)
  ]
  all_char = capital + lowercase + numbers + special_char
  password.extend(random.choices(all_char, k = 8))
  random.shuffle(password)
  
  return ''.join(password)
  

  