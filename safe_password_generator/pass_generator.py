import os
import random

def initial_screen():
  os.system('clear')
  print('''🅢🅐🅕🅔 🅟🅐🅢🅢 🅖🅔🅝     
(𝚂𝚊𝚏𝚎 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛)''')

def random_alpha():
  alpha = 'a b c d e f g h i j k l m n o p q r s t u v x y z'
  alpha_list_lower = alpha.split(' ')
  appha_list_upper = alpha.upper().split(' ')
  alpha_list = alpha_list_lower + appha_list_upper
  return random.choice(alpha_list)

def random_number():
  number = '1 2 3 4 5 6 7 8 9'
  number_list = number.split(' ')
  return random.choice(number_list)

def random_character():
  character = '# @ % & * ! _ - + = { } [ ] . ; , / ?'
  character_list = character.split(' ')
  return random.choice(character_list)

def create_pass():
  num_of_digits = int(input("What is the length of the password to be generated: "))
  password = ''
  while len(password) < num_of_digits: 
    options = [random_alpha(), random_number(), random_character()]
    item = random.choice(options)
    password += item
  return password
      
    
    
  
  



  