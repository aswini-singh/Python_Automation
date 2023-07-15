
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








