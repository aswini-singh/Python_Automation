from locale import currency
import requests
import json

currency_code = input("From_Currency_Code: ").lower()
cache = {}

while True:
    currency_exchange = input("To_Currency_Code: ").lower()

    if currency_exchange == '':
        break

    try:
        amount_to_exchange = int(input("Amount : "))

    except ValueError:
        print("Invalid input for amount. Please enter a valid number.")
        continue

    URL = f'http://www.floatrates.com/daily/{currency_code}.json'
    exch = json.loads(requests.get(URL).text)

    if currency_code == 'usd':
        cache.update(eur=exch['eur']['rate'])
    elif currency_code == 'eur':
        cache.update(usd=exch['usd']['rate'])
    else:
        cache.update(usd=exch['usd']['rate'], eur=exch['eur']['rate'])

    print("Checking the cache...")
    if currency_exchange in cache:
        rate = round(amount_to_exchange * cache[currency_exchange], 2)
        print("Oh! It is in the cache!")
        print(f"You received {rate} {currency_exchange.upper()}.")
    else:
        cache[currency_exchange] = exch[currency_exchange]['rate']
        rate = round(amount_to_exchange * cache[currency_exchange], 2)
        print(f"You received {rate} {currency_exchange.upper()}.")
