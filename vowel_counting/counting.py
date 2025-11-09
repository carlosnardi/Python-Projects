# Challenge:

# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

# Exemplo de entrada:
# Digite um texto: A linguagem Python é muito versátil.  

# Saída esperada:
# O texto contém 13 vogais.

def prepare_text(sentence):
  to_change = 'áéíóúãẽĩõũâêîôû'
  for char in to_change:
    if char in sentence:
      sentence = sentence.replace(char,'a')
  return sentence.lower()

def check_vowel_number(text):
  sentence = prepare_text(text)
  vowels = 'aeiou'
  num_of_vowels = 0
  for letter in sentence:
    if letter in vowels:
      num_of_vowels += 1
  return num_of_vowels
