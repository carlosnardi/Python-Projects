
def prepare_sentence(sentence):
  characters = ".,!?:;\"'()[]{}"
  for char in sentence:
    if char in characters:
      sentence = sentence.replace(char,"")    
  sentence = sentence.lower().strip().split()
  words_dict = {}
  for word in sentence:
    if word not in words_dict:
      words_dict[word] = 1
    else:
      words_dict[word] += 1
  return words_dict

def words_count(sentence):
  sentence_treated = prepare_sentence(sentence)
  num_of_words = len(sentence_treated)
  return num_of_words, sentence_treated
