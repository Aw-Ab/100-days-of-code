import requests
import pandas
import datetime
import json
exchange_rates = []

now = datetime.datetime.now()

if now.minute in [ 0 , 15 , 30 , 45 ] :
    r = requests.get(url="https://v6.exchangerate-api.com/.....") #enter your api token here 
    r.raise_for_status()
    exchange_rates = r.json()['conversion_rates']
    with open("cache/conversion_rates_now.json" , "w") as file :
         json.dump(exchange_rates , file , indent=4)

else :
    with open("cache/conversion_rates_now.json" , "r") as file :
        exchange_rates = json.load(file)




currency_code = pandas.read_csv("data/codes-all.csv", usecols=["AlphabeticCode" , "Currency"])
currency_code = currency_code.to_dict("records")






