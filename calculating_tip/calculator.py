
def prepare_input():
  print('-- Tip Calculator --\n')
  
  value_to_pay = input('Enter the bill amount: ')
  tip_value = input('Enter the tip percentage: ')
  if ',' in value_to_pay:
    value_to_pay = float(value_to_pay.replace(',','.'))
  else:
    value_to_pay = float(value_to_pay)
  if ',' in tip_value:
    tip_value = float(tip_value.replace(',', '.'))
  else:
    tip_value = float(tip_value)

  return value_to_pay, tip_value
    

def calc_tip():
  values = prepare_input()
  value_to_pay = values[0]
  tip_value = values[1]
  tip = round(value_to_pay * (tip_value / 100), 2)
  total_bill = round((value_to_pay + tip), 2)
  return total_bill, tip
  