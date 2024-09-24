import requests

api_key = 'your_api_key'
city = 'New York'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

for forecast in data['list']:
    print(f"Date: {forecast['dt_txt']}")
    print(f"Weather: {forecast['weather'][0]['description']}")
    print(f"Temperature: {forecast['main']['temp']}K")
    print()
