import requests

url = 'https://gist.githubusercontent.com/kalinchernev/486393efcca01623b18d/raw/daa24c9fea66afb7d68f8d69f0c4b8eeb9406e83/countries'

response = requests.get(url)

print(response.ok)

print(type(response.text))

with open("country_name.txt", 'w') as f:
    f.write(response.text)
