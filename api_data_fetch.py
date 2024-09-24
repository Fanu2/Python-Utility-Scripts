import requests

api_url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(api_url)
data = response.json()

for item in data:
    print(item)
