from transformers import pipeline

# Load pre-trained question answering model
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# input text
text = "John, 35 years old, suffers from chronic back pain and is on Ibuprofen."

# Extract named entities
entities = nlp(text)
print("Entities:")
for entity in entities:
    print(entity)