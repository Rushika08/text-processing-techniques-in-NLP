import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download the 'punkt' tokenizer
nltk.download('punkt')

def stem_Sentence(sentence):
    token_words = word_tokenize(sentence)  # Tokenize the sentence into individual words
    stem_Sentence = []  # Create an empty list to store stemmed words

    for word in token_words:
        stem_Sentence.append(PorterStemmer().stem(word))  # Apply stemming using the Porter stemmer
        stem_Sentence.append(" ")  # Add a space after each stemmed word

    return "".join(stem_Sentence)  # Join the stemmed words together into a sentence

input_sent = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
output_sent = stem_Sentence(input_sent)  # Apply stemming to the sentence
print(output_sent)  # Print the stemmed sentence


