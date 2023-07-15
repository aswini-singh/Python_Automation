
# Convert the Currency to one to another Country
#import the modules we need for coding
import requests

class Currency_convertor:
    #declare empty dict to store the convertion rates
    rates = {}
    def __init__(self,url):
        data = requests.get(url).json()
        #Extract only rates from json data
        self.rates = data["rates"]

    def Convertor(self,From_currency , To_currency , Amount):
        initial_amount = Amount
        if From_currency != "EUR":
            Amount = Amount / self.rates[From_currency]
        Amount = round(Amount * self.rates[To_currency],2)
        print(' {}{} = {}{} '.format(initial_amount,From_currency,Amount,To_currency))

if '__name__' == '__main__' :

    url = str.__add__('http://data.fixer.io/api/latest?access_key', YOUR_ACCESS_KEY)
    c = Currency_convertor(url)
    From_currency = input("FROM CURRENCY : ")
    To_currency = input("TO CURRENCY : ")
    Amount = int(input("AMOUNT : "))
    c.Convertor(From_currency , To_currency , Amount)







import tkinter as tk
import requests
import json

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.currency_code_label = tk.Label(self.root, text="From_Currency_Code:")
        self.currency_code_label.pack()
        self.currency_code_entry = tk.Entry(self.root)
        self.currency_code_entry.pack()

        self.currency_exchange_label = tk.Label(self.root, text="To_Currency_Code:")
        self.currency_exchange_label.pack()
        self.currency_exchange_entry = tk.Entry(self.root)
        self.currency_exchange_entry.pack()

        self.amount_label = tk.Label(self.root, text="Amount:")
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
            self.result_label.config(text="Invalid input for amount. Please enter a valid number.", fg="red")
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
            self.result_label.config(text=f"Oh! It is in the cache!\nYou received {rate} {currency_exchange.upper()}.",
                                     fg="green")
        else:
            self.cache[currency_exchange] = exch[currency_exchange]['rate']
            rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
            self.result_label.config(text=f"You received {rate} {currency_exchange.upper()}.", fg="blue")

root = tk.Tk()
converter = CurrencyConverter(root)
root.mainloop()
