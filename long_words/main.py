

### Challenge: 

# Write a program that receives a text and displays all words that have more than 10 letters. If no long words are found, the program should notify the user.

# Example input:
# Enter a text: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais

# Expected output:
# Long words found: programação, estruturada, desenvolvimento, computacionais

# If no long words are found: No long words were found in the text.

text = 'A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais'

# First Option:
def check_long_words(text):
  text = text.split(' ')
  long_words = []
  for item in text:
    if len(item) >= 10:
      long_words.append(item)
  return long_words

def print_long_words(text):
  list_of_words = check_long_words(text)
  if list_of_words == []:
    result = 'No long words were found in the text.'
  else:
    result = 'Long words found: '
    for item in list_of_words:
      if result == 'Long words found: ':
        result += item  
      else:
        result = result + (', ' + item)
  return result
  
print(print_long_words(text))


# Second Option:
# txt = text.split(' ')
# long_words2 = []
# for item in txt:
#   if len(item) >= 10:
#     long_words2.append(item)
#   else: 
#     pass

# result = 'Long words found: '
# if long_words2 == []:
#   result = 'No long words were found in the text.'
# else: 
#   for item in long_words2:
#     if result == 'Long words found: ':
#       result += item  
#     else:
#       result = result + (', ' + item)

# print(result)