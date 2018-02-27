# stop is part of preprocessing

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english')) # use english

# print(stop_words) # print the actual english stop words

word_tokens = word_tokenize(example_sent)

# could use one line instead of for function
#filtered_sentence = [w for w in word_tokens if not w in stop_words] 

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
