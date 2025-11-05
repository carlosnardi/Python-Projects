# from word_counter.words_count import words_count 
from word_counter import words_count

phrase = input('Type a sentence to count the words: ') 

number_of_words = words_count.words_count(phrase)

print(f'\nThe sentence has {number_of_words[0]} word') if number_of_words[0] == 1 else print(f'The sentence has {number_of_words[0]} words')

print('\nWord Count: ')
for item in number_of_words[1]:
  print(f'{item}: {number_of_words[1][item]}')


