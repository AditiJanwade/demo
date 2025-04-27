import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Input text (sentence)
text = "The quick brown fox jumps over the lazy dog."

# Process the text
doc = nlp(text)

# Print the POS tags for each token
for token in doc:
    print(f"{token.text}: {token.pos_}")
 