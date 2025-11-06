# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

# Exemplo de entrada:

# Digite o valor da conta: 120.00  
# Digite a porcentagem de gorjeta: 10  

# Saída esperada:

# Valor da gorjeta: R$ 12.00  
# Total a pagar: R$ 132.00  

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