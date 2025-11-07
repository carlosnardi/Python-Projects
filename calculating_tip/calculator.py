
def prepare_input():
  print('-- Tip Calculator --\n')
  value_to_pay = input('Enter the bill amount: ')
  tip_value = input('Enter the tip percentage: ')   
  items = [value_to_pay, tip_value]
  for i, item in enumerate(items):
    if ',' in item:
      items[i] = float(item.replace(',','.'))
    else:
      items[i] = float(item)
  return items

def calc_tip():
  values = prepare_input()
  value_to_pay, tip_value = values
  tip = round(value_to_pay * (tip_value / 100), 2)
  total_bill = value_to_pay + tip
  return total_bill, tip
  