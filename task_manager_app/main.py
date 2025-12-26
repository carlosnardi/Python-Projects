# Ana needs a simple program to manage her daily tasks. She wants to be able to add, view, and remove tasks from a list.

# Create a program with an interactive menu that allows the user to add, view, and remove tasks. Use a list to store the tasks.

# Example input:

# 1. Add task
# 2. View tasks
# 3. Remove task
# 4. Exit
# Choose an option: 1

# Expected output:

# Enter the task: Study Python
# Task added!

# If option 2 is selected when adding a task:

# Tasks:

# 1. Study Python

# If option 3 is selected with a task added:

# Enter the number of the task to be removed: 1
# Task 'Study Python' removed!

# If option 3 is selected without a task added:

# Enter the number of the task to be removed: Study Python
# Error: No tasks to remove.

# If you select option 3 with an invalid option:

# Choose an option: 3
# Enter the task number to be removed: ABC
# Error: Invalid entry! Enter a number.

# If you select none of the listed options:

# Choose an option: 5
# Error: Invalid option! Choose an option between 1 and 4.

# If you select option 4:

# Choose an option: 4 Exiting Task Manager. Goodbye!

from task_manager_app import task_operator as to

while True:
  try: 
    option = to.app_view()
    if option == 1:
      to.add_task()
    elif option == 2:
      to.list_tasks(to.LIST_OF_TASKS)
      to.press_return()
    elif option == 3: 
      to.remove_task(to.LIST_OF_TASKS)
      to.press_return()
    elif option == 4:
      print('Exiting Task Manager. Goodbye!')
      break
    else: 
      to.option_error_and_return()
  except ValueError:
    to.option_error_and_return()
