import spacy
 
nlp = spacy.load("en_core_web_sm")

def ner(text):
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

text = "Barack Obama was born in Hawaii and served as the 44th President of the United States."

print(ner(text))
