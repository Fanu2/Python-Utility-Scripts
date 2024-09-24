import requests

data = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=data)
print(response.status_code)
print(response.json())
