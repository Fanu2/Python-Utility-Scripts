import requests

def convert_currency(amount, from_currency, to_currency):
    api_url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(api_url)
    rates = response.json()['rates']
    return amount * rates[to_currency]

amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is {converted_amount} {to_currency}')
