def analyze_text(text_file, word_file):

  with open(text_file, 'r') as f:
    text = f.read().lower()  

  import re
  words = re.findall(r'\w+', text)

  word_count = len(words)
  unique_word_count = len(set(words))

  with open(word_file, 'r') as f:
    correctly_spelled_words = set(line.strip().lower() for line in f) 

  misspelled_words = [word for word in words if word not in correctly_spelled_words]

  return {
      'word_count': word_count,
      'unique_word_count': unique_word_count,
      'misspelled_words': misspelled_words
  }

results = analyze_text("alice.txt", "words.txt")

print(f"Count Word: {results['word_count']}")
print(f"Unique Word: {results['unique_word_count']}")
print(f"Missspelled Word: {results['misspelled_words']}")