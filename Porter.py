# tokenizing words and sentences 
# stemming is a form of data pre-processing

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 

# could it be faster if i use sent_tokenize? 

ps = PorterStemmer()

# first stem words
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w)) #print the stem of the words

# stem some sentences
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w)) #print the stemmed sentence
