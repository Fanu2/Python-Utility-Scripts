import requests

def get_weather_alert(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['weather'][0]['main'] in ['Storm', 'Rain']:
        return f"Weather alert for {city}: {data['weather'][0]['description']}"
    return None

api_key = 'your_api_key'
city = 'New York'
alert = get_weather_alert(api_key, city)
if alert:
    print(alert)
