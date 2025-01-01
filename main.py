import requests
import json

#this code get latest bitcoin usd price provided by coindesk
#just run the code and see the result
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

x = requests.get(url)

y = json.loads(x.text)

price = y['bpi']['USD']["rate"]

time = y['time']['updated']

print("the price of bitcoin is $" + price)
print("updated: " + time)