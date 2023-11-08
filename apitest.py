import requests
import csv
import pandas as pd
from bsedata.bse import BSE
import requests
import json
import pandas as pd
b = BSE()
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=500325&apikey=2RRRXZ40FC0VS0G6&datatype=json'
# r = requests.get(url)
# data= r.json()

# print(data)
q = b.getQuote('532880')
print(q)
date = q['updatedOn']
curr = q['currentValue']
open_price = q['previousOpen']
high = q['dayHigh']
low = q['dayLow']
close = q['currentValue']


lis = [[date, open_price, high, low, close, 0, 0,0, 0, 0, 0, 0, 0 ]]
import csv


csv_ = 'data_more/500002 (1).csv'
cs = pd.read_csv(csv_)
with open(csv_, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lis)
print(cs['Date'])
#his = b.getPeriodTrend('534976','6M')

#print(his)
# url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE:540602&outputsize=full&apikey=2RRRXZ40FC0VS0G6"
# r = requests.get(url)
# #  {'date': 'Fri Feb 12 2021 00:00:00', 'value': '2881.35', 'vol': '8452'}]
# data = r.json()

# print(data)