# The PunktSentenceTokenizer is capable of unsupervised machine learning
# Train it on any body of text I want

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# create training and testing data
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# train the Punkt tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# and then tokenize
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# run through and tag all the parts of speech per sentence
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content() # output a list of tuples (word, POS tag)
