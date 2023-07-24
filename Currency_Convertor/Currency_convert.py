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
        self.amount_label.grid(row=2, column=0, padx=8, pady=8)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=2, column=1, padx=8, pady=8)

        self.convert_button = tk.Button(input_frame, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a font with desired size and bold style
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 22, "bold"))  # Apply the font to the label
        self.result_label.pack()

    def center_window(self, win, width, height):
        # Get the screen width and height
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Set the window's position
        win.geometry(f"{width}x{height}+{x}+{y}")

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
        # Fetch exchange rates using the 'currency_code' as the base currency

        URL = f'http://www.floatrates.com/daily/{currency_code}.json'
        response = requests.get(URL)
        if response.status_code != 200:
            self.result_label.config(text="Failed to fetch exchange rates. Please try again later.")
            return

        try:
            exch = response.json()
            self.cache.update({cur.lower(): exch[cur.lower()]['rate'] for cur in exch})

            print("Checking the cache...")
            if currency_exchange in self.cache:
                rate = round(amount_to_exchange * self.cache[currency_exchange], 2)
                self.result_label.config(text=f"Hi! You will receive {rate} {currency_exchange.upper()}.",
                                         fg="green")
            
            else:
                self.result_label.config(text="Invalid currency code. Please enter a valid currency code.")
        except (json.JSONDecodeError, KeyError):
            self.result_label.config(text="Failed to process exchange rates. Please try again later.")

root = tk.Tk()
converter = CurrencyConverter(root)
converter.center_window(root, 400, 250)  # Set the width and height for the main window
root.mainloop()
