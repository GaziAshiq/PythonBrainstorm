import spacy
import json

# Initialize SpaCy
nlp = spacy.load("en_core_web_sm")

# Example JSON data
conversation_data = {}

# Function to process input text and update JSON
def process_text(text):
    global conversation_data
    doc = nlp(text)
    for ent in doc.ents:
        # Update JSON with new entities
        conversation_data[ent.label_] = ent.text
    return conversation_data

# Example usage
user_input = "Patient John is 35 years old and has chronic back pain."
updated_json = process_text(user_input)
print("Updated Conversation Data:")
print(json.dumps(updated_json, indent=4))
