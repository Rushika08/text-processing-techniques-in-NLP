import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict

# Download required resources
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Create a mapping from POS tags to WordNet tags
tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

text = "guru99 is a totally new kind of learning experience."       # Define the input text
tokens = word_tokenize(text)     # Tokenize the text into words
lemma_function = WordNetLemmatizer()    # Initialize the WordNet Lemmatizer

# Lemmatize each token based on its POS tag
for token, tag in pos_tag(tokens):
    lemma = lemma_function.lemmatize(token, tag_map[tag[0]])        # Lemmatize the token using the appropriate WordNet tag from the mapping
    print(token, "=>", lemma)       # Print the original token and its lemma