#Script to get all ticker data
#Run frequency: 1st of each month
#Run time: 3:00 am IST
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json

#Gathering data from API
response = requests.get('http://api.marketstack.com/v1/tickers?access_key=7a247f5ee1c585714c83b74587866efb&exchange=XNSE')
jsonResponse = response.json()
#Making panda dataframe

df = pd.DataFrame(jsonResponse['data']) 
df = df[['symbol', 'name']]
df.sort_values(by='symbol', ascending=1, inplace=True)
df.to_csv('/home/moumita_das2820/StockPredict/data/ticker.csv',index=False)

