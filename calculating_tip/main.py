from calculating_tip import calculator

start = True
while start:
  try:
    result = calculator.calc_tip()
    print(f'''
  Tip amount: $ {result[1]:.2f}
  Total: $ {result[0]:.2f}''')
  except:
    print("Error: Try again. Enter only numbers")
  start = input("\nPress Enter to reload or any key to exit \n") 
  start = True if start == "" else start == False

