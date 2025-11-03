from word_counter.words_count import words_count

phrase = input('Type a sentence to count the words: ')

#words_list = phrase.split()
#print(len(words_list))

phrase = words_count(phrase)

print(f'The phrase has {phrase} words')