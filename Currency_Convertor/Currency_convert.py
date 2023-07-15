# convert currency codes...
#USD: United States Dollar
# EUR: Euro
# GBP: British Pound Sterling
# JPY: Japanese Yen
# CAD: Canadian Dollar
# AUD: Australian Dollar
# CHF: Swiss Franc
# CNY: Chinese Yuan Renminbi
# INR: Indian Rupee
# MXN: Mexican Peso


import tkinter as tk
import requests
import json

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.currency_code_label = tk.Label(self.root, text="From_Currency_Code: ")
        self.currency_code_label.pack()
        self.currency_code_entry = tk.Entry(self.root)
        self.currency_code_entry.pack()

        self.currency_exchange_label = tk.Label(self.root, text="To_Currency_Code: ")
        self.currency_exchange_label.pack()
        self.currency_exchange_entry = tk.Entry(self.root)
        self.currency_exchange_entry.pack()

        self.amount_label = tk.Label(self.root, text="Amount: ")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        self.cache = {}

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def convert_currency(self):
        currency_code = self.currency_code_entry.get().lower()
        currency_exchange = self.currency_exchange_entry.get().lower()

        if currency_exchange == '':
            return

        try:
            amount_to_exchange = int(self.amount_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input for amount. Please enter a valid number.")
            return

        URL = f'http://www.floatrates.com/daily/{currency_code}.json'
        exch = json.loads(requests.get(URL).text)

        if currency_code == 'usd':
            self.cache.update(eur=exch['eur']['rate'])
        elif currency_code == 'eur':
            self.cache.update(usd=exch['usd']['rate'])
            

        else:
            self.cache.update(usd=exch['usd']['rate'], eur=exch['eur']['rate'])

        print("Checking the cache...")
        if currency_exchange in self.cache:
            rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
            self.result_label.config(text=f"Oh! It is in the cache!\nYou received {rate} {currency_exchange.upper()}.", fg = "green")
        else:
            self.cache[currency_exchange] = exch[currency_exchange]['rate']
            rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
            self.result_label.config(text=f"You received {rate} {currency_exchange.upper()}.",fg = "red"  )

root = tk.Tk()
converter = CurrencyConverter(root)
root.mainloop()
