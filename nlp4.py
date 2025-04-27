import nltk
from nltk.corpus import wordnet as wn

# Download required NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')  # Optional: For multilingual WordNet
# Function to get semantic relationships
def get_semantic_relationships(word1, word2):
    # Get synsets for the words
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)
    if not synsets1 or not synsets2:
        return f"Semantic relationships could not be determined for '{word1}' and '{word2}'."
    # Display relationships for the first synset of each word
    synset1 = synsets1[0]
    synset2 = synsets2[0]
    relationships = {
        "Word 1": word1,
        "Word 2": word2,
        "Synset 1 Definition": synset1.definition(),
        "Synset 2 Definition": synset2.definition(),
        "Similarity Score": synset1.wup_similarity(synset2),  # Wu-Palmer Similarity
        "Hypernyms of Word 1": [lemma.name() for hypernym in synset1.hypernyms() for lemma in hypernym.lemmas()],
        "Hypernyms of Word 2": [lemma.name() for hypernym in synset2.hypernyms() for lemma in hypernym.lemmas()],
        "Hyponyms of Word 1": [lemma.name() for hyponym in synset1.hyponyms() for lemma in hyponym.lemmas()],
        "Hyponyms of Word 2": [lemma.name() for hyponym in synset2.hyponyms() for lemma in hyponym.lemmas()],
    }
    return relationships
# Example Usage
word1 = "dog"
word2 = "cat"
semantic_relationships = get_semantic_relationships(word1, word2)
# Print results
for key, value in semantic_relationships.items():
    print(f"{key}: {value}")
