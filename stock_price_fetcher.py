import requests

def fetch_stock_price(symbol):
    url = f'https://api.example.com/stocks/{symbol}'
    response = requests.get(url)
    data = response.json()
    return data['price']

symbol = 'AAPL'
price = fetch_stock_price(symbol)
print(f'The price of {symbol} is ${price}')
