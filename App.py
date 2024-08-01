import requests

API_KEY = '86975d48f084e78097e40cbc'
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

def convert_currency(amount, from_currency, to_currency):
    url = f"{BASE_URL}{API_KEY}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data['conversion_rates']
        if to_currency in rates:
            converted_amount = amount * rates[to_currency]
            print(f"{amount} {from_currency} = {converted_amount:2f} {to_currency}")
        else:
            print("Target currency not found")
    else:
        print("Error fetching conversion rates.")

amount = float(input("Enter amount to convert: "))
from_currency = input("Enter currency from: ")
to_currency = input("Enter currency to: ")
convert_currency(amount, from_currency, to_currency)