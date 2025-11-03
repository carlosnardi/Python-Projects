words = 'Hello world'

for letter in words:
  if letter == 'l':
    words = words.replace('l', 'b')

print(words)