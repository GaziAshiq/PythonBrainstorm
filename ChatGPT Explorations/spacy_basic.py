import spacy  # Importing the library

nlp = spacy.load("en_core_web_lg")  # Loading the model

# Example text
text = "Patient John, 35 years old, has chronic back pain and is a heavy smoker."

doc = nlp(text)  # Processing the text

# Extracting entities
print("Entities:")
for ent in doc.ents:
    print(f'{ent.text} {ent.label_}')

# Extracting tokens
print("\nTokens:")
for token in doc:
    print(token.text)
