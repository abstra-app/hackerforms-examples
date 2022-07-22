from hackerforms import *
import requests
import json

display("Hey there. Welcome to our currency converter.")

head = {}
data = {}
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json'
response = requests.get(url, json=data, headers=head)
response = response.json()
list = response['usd']

currencies = []
for item in list:
    currencies.append(item)

page = Page().read_number("What's the USD amount you'd like to convert?") \
             .read_dropdown("Select the currency you need:",
             options=currencies) \
             .run("Next")
amount, currency = page.values()

currency_value = list[currency]
conversion = amount * currency_value

display(f"Your amount of ${amount} is currently equal to {conversion} {currency}.", button_text = "See you next time")
