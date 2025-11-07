

def prepare_id():
  id_number = input("Enter your ID: ")
  characters = './- '
  for char in characters: 
    if char in id_number:
      id_number = id_number.replace(char, '')  
  return id_number

def check_id():
  id = prepare_id()
  try: 
    id_check = int(id)
    if len(id) == 11: 
      return print('Valid ID')
    else: 
      return print('Error: The ID must have eleven numbers')
  except: 
    return print('Enter only numbers')