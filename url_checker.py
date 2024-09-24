import requests

def check_url(url):
    response = requests.get(url)
    return response.status_code

url = 'https://example.com'
status = check_url(url)
print(f'The status code for {url} is {status}')
