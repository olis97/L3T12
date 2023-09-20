# Import spacy
import spacy

# Load sm
nlp = spacy.load('en_core_web_sm')

# Tokenize using sm
tokens = nlp('cat apple monkey banana ')

print("\n\nWORD EXAMPLE: Compare words using 'en_core_web_md'...\n")

# Loop through each token & print similarities
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Load md
nlp = spacy.load('en_core_web_md')

# Tokenize using md
tokens = nlp('cat apple monkey banana ')

print("\n\nComparing words using 'en_core_web_md'...\n")

# Loop through each token & print similarities
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n\nUSING SENTENCES EXAMPLE: Compare sentences using 'en_core_web_md'...\n")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Tokenization using md
model_sentence = nlp(sentence_to_compare)
# Loop through each token & print similarities
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# My own example for the similarity between: 
#   Microsoft Windows, Apple iOS and Linux
print("\n\nMY OWN EXAMPLE: Compare words using 'en_core_web_md'...\n")

# Tokenize words
token_words = nlp('Windows Apple Linux')

for word1 in token_words:
    for word2 in token_words:
        print(word1.text, word2.text, word1.similarity(word2))
    