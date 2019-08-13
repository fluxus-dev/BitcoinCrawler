import requests

host = 'https://api.bithumb.com/public/'
currency = 'BTC'


def get_ticker():
    url = host + 'ticker/' + currency
    return requests.get(url)


def get_order_book():
    url = host + 'orderbook/' + currency
    return requests.get(url)
