import json

# JSON data
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "conditinos": ["back pain", "smoker"]
}

# Writing JSON data
json_data = json.dumps(data, indent=4)
print("JSON data:")
print(json_data)

# Reading JSON data
parsed_data = json.loads(json_data)
print("\nPython dictionary:")
print(parsed_data)

# updating json data
parsed_data["new symptom"] = ["headache", "cough"]

# Writing updated JSON data
updated_json_data = json.dumps(parsed_data, indent=4)
print("\nUpdated JSON data:")
print(updated_json_data)