import requests

api_url = 'https://api-ssl.bitly.com/v4/shorten'
access_token = 'your_access_token'
long_url = 'https://example.com'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
data = {
    'long_url': long_url
}
response = requests.post(api_url, headers=headers, json=data)
short_url = response.json().get('link')

print(f"Short URL: {short_url}")
