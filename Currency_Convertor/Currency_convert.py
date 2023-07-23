import tkinter as tk
import requests
import json


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.cache = {}

        # Create a frame to hold the labels and entry widgets
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=20, pady=10)

        self.currency_code_label = tk.Label(input_frame, text="FromCurrencyCode:")
        self.currency_code_label.grid(row=0, column=0, padx=5, pady=5)
        self.currency_code_entry = tk.Entry(input_frame)
        self.currency_code_entry.grid(row=0, column=1, padx=5, pady=5)

        self.currency_exchange_label = tk.Label(input_frame, text="ToCurrencyCode:")
        self.currency_exchange_label.grid(row=1, column=0, padx=5, pady=5)
        self.currency_exchange_entry = tk.Entry(input_frame)
        self.currency_exchange_entry.grid(row=1, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(input_frame, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

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
        response = requests.get(URL)
        if response.status_code != 200:
            self.result_label.config(text="Failed to fetch exchange rates. Please try again later.")
            return

        try:
            exch = response.json()
            if currency_code == 'eur':
                self.cache.update(inr=exch['inr']['rate'])
            else:
                self.cache.update(inr=exch['eur']['rate'], eur=exch['eur']['rate'])

            print("Checking the cache...")
            if currency_exchange in self.cache:
                rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
                self.result_label.config(text=f"Hi! You will receive {rate} {currency_exchange.upper()}.",
                                         fg="green")
            else:
                if currency_exchange in exch:
                    self.cache[currency_exchange] = exch[currency_exchange]['rate']
                    rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
                    self.result_label.config(text=f"You will receive {rate} {currency_exchange.upper()}.", fg="red")
                else:
                    self.result_label.config(text="Invalid currency code. Please enter a valid currency code.")
        except (json.JSONDecodeError, KeyError):
            self.result_label.config(text="Failed to process exchange rates. Please try again later.")


root = tk.Tk()
converter = CurrencyConverter(root)
root.mainloop()
