
def prepare_sentence(sentence):
  result = sentence.lower().strip().split()
  return result

def words_count(sentence):
  sentence_treated = prepare_sentence(sentence)
  num_of_words = len(sentence_treated)
  return num_of_words
  
  