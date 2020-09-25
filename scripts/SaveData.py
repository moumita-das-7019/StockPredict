#Script to get clsoing price of all stock data
#Run frequency: Everyday
#Run time: 3:30 am IST
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json
import time

#Gater ticker informations
tickers = pd.read_csv('/home/moumita_das2820/StockPredict/data/ticker.csv')
noData = []
#Function to save stock closing data

def StockDataSaver(stock):
            access_key='7a247f5ee1c585714c83b74587866efb'
            url='http://api.marketstack.com/v1/eod?access_key='+access_key+ '&symbols=' + stock +'&%20date_from=2000-01-01&limit=1000'
            response = requests.get(url)
            jsonResponse = response.json()
            if jsonResponse['data']:
                df = pd.DataFrame(jsonResponse['data']) 
                df = df[['date','close', 'open', 'adj_close']]
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d''T''%H:%M:%S+%f')
                df.set_index('date', inplace = True)
                df.sort_values(by='date', ascending=1, inplace=True)
                df.to_csv('/home/moumita_das2820/StockPredict/data/'+stock+'.csv')
            else:
                noData.append(stock)
            time.sleep(15) #API requests for this website doesn't allow more than 5 calls/minute

#Save each stock data
for stock in tickers['symbol']:
            StockDataSaver(stock)

#Recreate ticker.csv if stock data is not present
if noData:
        tickers = tickers.set_index("symbol")
        tickers = tickers.drop(noData, axis=0)
        new_tickers = tickers.reset_index()
        new_tickers.to_csv("/home/moumita_das2820/StockPredict/data/ticker.csv")

