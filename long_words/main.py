

### Challenge: 

# Write a program that receives a text and displays all words that have more than 10 letters. If no long words are found, the program should notify the user.

# Example input:
# Enter a text: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais

# Expected output:
# Long words found: programação, estruturada, desenvolvimento, computacionais

# If no long words are found: No long words were found in the text.

text = 'A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais'

text = text.split(' ')
extensive_words = []
for item in text:
  if len(item) >= 10:
    extensive_words.append(item)

print(extensive_words)

