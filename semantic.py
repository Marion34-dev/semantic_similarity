# Running all code extracts: code extracts deleted not to crowd the py file

# Running code comparing the words: cat, monkey, apple and banana and commenting on results
import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        # Interesting similarity found between cat and monkey, i.e. both animals
        # Interesting similarity found as well between monkey and banana, suggesting a link between the two
        # (i.e. the monkey eats bananas)

# My own example
words = nlp('house bungalow sun kitchen')

for word1 in words:
    for word2 in words:
        print(word1.text, word2.text, word1.similarity(word2))
        # Similarity found between house and bungalow, both being buildings for human habitation
        # Similarity found between house/bungalow and kitchen, as these buildings tend to have kitchens
        # Sun on the other hand does not show much similarity with either

# Running the example file with the 'en_core_web_sm' and 'en_core_web_smd' language models
    # A UserWarning [W007] message indicating that the sm language model has no word vectors loaded
    # Indeed, the 'en_core_web_sm' (small) model doesn't ship with word vector and only use context-sensitive tensors
    # The similarity method will therefore be based on the tagger, parser and NER which may not yield accurate results
    # SOLUTIONS: use of a larger model if available (sm model works here), or the user should add their own word vectors
