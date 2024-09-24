import requests

api_key = 'your_api_key'
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

print(f"Weather in {city}: {data['weather'][0]['description']}")
print(f"Temperature: {data['main']['temp']}K")
