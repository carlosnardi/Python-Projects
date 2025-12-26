import os

LIST_OF_TASKS = []

def app_view():
  os.system('clear')
  print('*** TASK MANAGER ***')
  print('''\nOptions: 
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Exit''')
  option = int(input('Choose an option: '))
  return option

def press_return():
  input('Press any key to return')

def option_error_and_return():
  print('Please try again, choose an option between 1 and 4.')
  press_return()

def add_task():
  task = input('Enter the task: ')
  LIST_OF_TASKS.append(task)
  return LIST_OF_TASKS

def list_tasks(LIST_OF_TASKS):
  if not LIST_OF_TASKS:
    print('No tasks')
  else: 
    for number, item in enumerate(LIST_OF_TASKS):
      print(f'{number+1}. {item}')

def remove_task(LIST_OF_TASKS):
  try: 
    list_tasks(LIST_OF_TASKS)
    to_remove = int(input('Enter the task number to be removed: '))
    item_removed = LIST_OF_TASKS.pop(to_remove -1)
    print(f"Task '{item_removed}' removed")
  except IndexError:
    if not LIST_OF_TASKS:
      print('Error: No tasks to remove')
    else: 
      print('Error: check the number to remove')
  except ValueError: 
    print('Error: Invalid entry! Enter a number.')
    

