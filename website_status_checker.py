import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f'{url} is up!')
    except requests.exceptions.RequestException as e:
        print(f'{url} is down! Error: {e}')

url = 'https://example.com'
check_website_status(url)
