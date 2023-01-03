import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)

# SKILL DRILL

text = word_tokenize("I love making pancakes in the morning while listening to music.")
output = nltk.pos_tag(text)
print(output)
