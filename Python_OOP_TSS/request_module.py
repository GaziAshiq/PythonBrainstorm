import requests
import os
import webbrowser as wb
url = 'https://www.activestate.com/resources/quick-reads/how-to-list-installed-python-packages/'

response = requests.get(url)


print(type(response))
print(response.ok)
print(response.status_code)
# print(response.text)
# print(type(response.text))


with open('python_env.html', 'w', encoding=response.encoding) as f:
    f.write(response.text)


file_path = os.path.relpath('python_env.html')
print(file_path)
wb.open('file://' + file_path)