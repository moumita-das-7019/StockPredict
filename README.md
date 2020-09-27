
# README.md

Stock Market Prediction Application

# About the project

This is a project to predict stock market closing price for future dates with LSTM model as its backbone.

## Document Version

| Version |Remarks  |
|--|--|
| 1.0 | First draft, documentation under development  |


## Software dependencies

1. Google instance: 
	a)Google Deep learning Linux image of version "TensorFlow 1.15.2 with CUDA 10.0 and Intel® MKL-DNNmachine 
	b)Machine type e2-highmem-4 (4 vCPUs, 32 GB memory)

This comes with default infra monitoring setup, tools installed liked tensorflow, reduces headache of environment setup.

2. Streamlit: A powerful python tool that gives an easy deployment of python application for web interface.

3. Python3 : Only programming language used here.

4. Git: Version control system

5. Cron: To Setup periodic data download, csv file creation, and model creation.

6. Panda: As data analysis and manipulation tool.

## Dataset 
Python scripts will be downloading json data from https://marketstack.com for individual stocks and convert them into useful panda dataset.
Storing format is .csv.
This website has data of 100+ Indian stocks accessible through APIs, but downside is with the free account, you shall get only data of 1 year.

## How to set up environment

On google deep learning image instance to setup environment:
1.Clone the repository.
> $git clone https://github.com/moumita-das-7019/StockPredict.git


2.Install required tools and libraries.
> $cd StockPredict 
> $pip install streamlit $python3 -m pip install -r requirements.txt --user #Installs  other library requirements

3.Setup API key to get data.

a) Login to https://marketstack.com and create free account
b)Store your API key for later use
c)Rename scripts/demosecret.py as secret.py and change "APIKeyValue" with your API key,

> def access_key():
>         return 'APIKeyValue'

This file is added to .gitignore file so that your API key is kept secret.

4.Create dataset.
> $python3 scripts/ticker.py  #To get all tickers of Indian Stock Exchange available  
> $python3 scripts/SaveData.py #To get all the stock price data of individual stocks 
> $exec python3 scripts/CreateModel.py #To save all the 
models of Individual stock.
We shall use exec so that terminal timeout doesn't cause the script to stop.

5.Run application

> $streamlit run StockPredict.py #Run the application and you get url
> for webbrowser

6.Access it on browser

> http://Exeternal_IP:8501

## Repository content

When writing this document, many of my models are yet to be produced, so model directory has less data than expected.

> $tree

.
├── data
│   ├── 3MINDIA.XNSE.csv
│   ├── ABB.XNSE.csv
│   ├── ACC.XNSE.csv
│   ├── ADANIENT.XNSE.csv
│   ├── ADANIGREEN.XNSE.csv
│   ├── ADANIPORTS.XNSE.csv
│   ├── ADANITRANS.XNSE.csv
│   ├── AMBUJACEM.XNSE.csv
│   ├── APOLLOHOSP.XNSE.csv
│   ├── ASIANPAINT.XNSE.csv
│   ├── AXISBANK.XNSE.csv
│   ├── BAJAJ_AUTO.XNSE.csv
│   ├── BAJAJFINSV.XNSE.csv
│   ├── BAJAJHLDNG.XNSE.csv
│   ├── BAJFINANCE.XNSE.csv
│   ├── BANDHANBNK.XNSE.csv
│   ├── BERGEPAINT.XNSE.csv
│   ├── BHARTIARTL.XNSE.csv
│   ├── BOSCHLTD.XNSE.csv
│   ├── BPCL.XNSE.csv
│   ├── BRITANNIA.XNSE.csv
│   ├── CADILAHC.XNSE.csv
│   ├── CHOLAFIN.XNSE.csv
│   ├── COALINDIA.XNSE.csv
│   ├── DABUR.XNSE.csv
│   ├── DIVISLAB.XNSE.csv
│   ├── DLF.XNSE.csv
│   ├── DMART.XNSE.csv
│   ├── DRREDDY.XNSE.csv
│   ├── EICHERMOT.XNSE.csv
│   ├── EMBASSY.RR.XNSE.csv
│   ├── GAIL.XNSE.csv
│   ├── GODREJCP.XNSE.csv
│   ├── GODREJPROP.XNSE.csv
│   ├── GRASIM.XNSE.csv
│   ├── GSKCONS.XNSE.csv
│   ├── HAL.XNSE.csv
│   ├── HAVELLS.XNSE.csv
│   ├── HCLTECH.XNSE.csv
│   ├── HDFCAMC.XNSE.csv
│   ├── HDFCBANK.XNSE.csv
│   ├── HDFCLIFE.XNSE.csv
│   ├── HDFC.XNSE.csv
│   ├── HEROMOTOCO.XNSE.csv
│   ├── HINDUNILVR.XNSE.csv
│   ├── HINDZINC.XNSE.csv
│   ├── ICICIBANK.XNSE.csv
│   ├── ICICIGI.XNSE.csv
│   ├── ICICIPRULI.XNSE.csv
│   ├── INDIGO.XNSE.csv
│   ├── INDUSINDBK.XNSE.csv
│   ├── INFRATEL.XNSE.csv
│   ├── INFY.XNSE.csv
│   ├── IOC.XNSE.csv
│   ├── IRCTC.XNSE.csv
│   ├── ITC.XNSE.csv
│   ├── JSWSTEEL.XNSE.csv
│   ├── KANSAINER.XNSE.csv
│   ├── KOTAKBANK.XNSE.csv
│   ├── LT.XNSE.csv
│   ├── MARICO.XNSE.csv
│   ├── MARUTI.XNSE.csv
│   ├── MCDOWELL_N.XNSE.csv
│   ├── NAM_INDIA.XNSE.csv
│   ├── NESTLEIND.XNSE.csv
│   ├── newticker.csv
│   ├── Newtickers.csv
│   ├── NHPC.XNSE.csv
│   ├── NMDC.XNSE.csv
│   ├── noData
│   ├── NTPC.XNSE.csv
│   ├── OFSS.XNSE.csv
│   ├── ONGC.XNSE.csv
│   ├── original_ticker.csv
│   ├── PAGEIND.XNSE.csv
│   ├── PETRONET.XNSE.csv
│   ├── PGHH.XNSE.csv
│   ├── PIDILITIND.XNSE.csv
│   ├── POWERGRID.XNSE.csv
│   ├── RECLTD.XNSE.csv
│   ├── RELIANCE.XNSE.csv
│   ├── SBILIFE.XNSE.csv
│   ├── SBIN.XNSE.csv
│   ├── SHREECEM.XNSE.csv
│   ├── SIEMENS.XNSE.csv
│   ├── SRF.XNSE.csv
│   ├── SRTRANSFIN.XNSE.csv
│   ├── SUNPHARMA.XNSE.csv
│   ├── TATAMOTORS.XNSE.csv
│   ├── TATASTEEL.XNSE.csv
│   ├── TCS.XNSE.csv
│   ├── TECHM.XNSE.csv
│   ├── TextData
│   ├── ticker.csv
│   ├── TITAN.XNSE.csv
│   ├── TORNTPHARM.XNSE.csv
│   ├── TRENT.XNSE.csv
│   ├── ULTRACEMCO.XNSE.csv
│   ├── UPL.XNSE.csv
│   ├── VBL.XNSE.csv
│   ├── VEDL.XNSE.csv
│   ├── VOLTAS.XNSE.csv
│   ├── WHIRLPOOL.XNSE.csv
│   ├── WIPRO.XNSE.csv
│   └── ZEEL.XNSE.csv
├── models
│   ├── 3MINDIA.XNSE_model
│   ├── ABB.XNSE_model
│   ├── ACC.XNSE_model
│   ├── ADANIENT.XNSE_model
│   ├── ADANIGREEN.XNSE_model
│   ├── ADANIPORTS.XNSE_model
│   ├── ADANITRANS.XNSE_model
│   ├── AMBUJACEM.XNSE_model
│   ├── APOLLOHOSP.XNSE_model
│   ├── ASIANPAINT.XNSE_model
│   ├── AXISBANK.XNSE_model
│   ├── BAJAJ_AUTO.XNSE_model
│   ├── BAJAJFINSV.XNSE_model
│   ├── BAJAJHLDNG.XNSE_model
│   ├── BAJFINANCE.XNSE_model
│   ├── BANDHANBNK.XNSE_model
│   ├── BERGEPAINT.XNSE_model
│   ├── BHARTIARTL.XNSE_model
│   ├── BOSCHLTD.XNSE_model
│   ├── BPCL.XNSE_model
│   ├── BRITANNIA.XNSE_model
│   ├── CADILAHC.XNSE_model
│   ├── CHOLAFIN.XNSE_model
│   ├── COALINDIA.XNSE_model
│   ├── DABUR.XNSE_model
│   ├── DIVISLAB.XNSE_model
│   ├── DLF.XNSE_model
│   ├── DMART.XNSE_model
│   ├── DRREDDY.XNSE_model
│   ├── EICHERMOT.XNSE_model
│   ├── EMBASSY.RR.XNSE_model
│   ├── GAIL.XNSE_model
│   ├── GODREJCP.XNSE_model
│   ├── GODREJPROP.XNSE_model
│   ├── GRASIM.XNSE_model
│   ├── GSKCONS.XNSE_model
│   ├── HAL.XNSE_model
│   ├── HAVELLS.XNSE_model
│   ├── HCLTECH.XNSE_model
│   ├── HDFCAMC.XNSE_model
│   ├── HDFCBANK.XNSE_model
│   ├── HDFCLIFE.XNSE_model
│   ├── HDFC.XNSE_model
│   ├── HEROMOTOCO.XNSE_model
│   ├── HINDUNILVR.XNSE_model
│   ├── HINDZINC.XNSE_model
│   ├── ICICIBANK.XNSE_model
│   ├── ICICIGI.XNSE_model
│   ├── ICICIPRULI.XNSE_model
│   ├── INDIGO.XNSE_model
│   ├── INDUSINDBK.XNSE_model
│   ├── INFRATEL.XNSE_model
│   ├── INFY.XNSE_model
│   ├── IOC.XNSE_model
│   ├── IRCTC.XNSE_model
│   ├── ITC.XNSE_model
│   ├── JSWSTEEL.XNSE_model
│   ├── KANSAINER.XNSE_model
│   ├── KOTAKBANK.XNSE_model
│   ├── LT.XNSE_model
│   ├── MARICO.XNSE_model
│   ├── MARUTI.XNSE_model
│   ├── MCDOWELL_N.XNSE_model
│   ├── NAM_INDIA.XNSE_model
│   ├── NESTLEIND.XNSE_model
│   ├── NHPC.XNSE_model
│   ├── NMDC.XNSE_model
│   ├── NTPC.XNSE_model
│   ├── OFSS.XNSE_model
│   ├── ONGC.XNSE_model
│   ├── PAGEIND.XNSE_model
│   ├── PETRONET.XNSE_model
│   ├── PGHH.XNSE_model
│   ├── PIDILITIND.XNSE_model
│   ├── POWERGRID.XNSE_model
│   ├── RECLTD.XNSE_model
│   ├── RELIANCE.XNSE_model
│   ├── SBILIFE.XNSE_model
│   ├── SBIN.XNSE_model
│   ├── SHREECEM.XNSE_model
│   ├── SIEMENS.XNSE_model
│   ├── SRF.XNSE_model
│   ├── SRTRANSFIN.XNSE_model
│   ├── SUNPHARMA.XNSE_model
│   ├── TATAMOTORS.XNSE_model
│   ├── TATASTEEL.XNSE_model
│   ├── TCS.XNSE_model
│   └── TECHM.XNSE_model
├── NextDayStockPredict.py
├── __pycache__
│   └── secret.cpython-37.pyc
├── README.md
├── requirements.txt
├── scripts
│   ├── CreateModel.py
│   ├── demosecret.py
│   ├── __pycache__
│   │   └── secret.cpython-37.pyc
│   ├── SaveData.py
│   ├── secret.py
│   └── ticker.py
├── StockMarket.jpg
├── Stock Market Prediction Application User Guide.pdf
├── Test
│   ├── myStockPredict.py
│   ├── newStockPredict.py
│   ├── StockPredict.py
│   ├── TCSModel.py
│   └── test_StockPredict.py
└── test.py

6 directories, 211 files


## How does the application work?

1. On 1st of month, cronjob configured on device gets all ticker data from the website is csv format.
2.  Every day another cronjob gets all the previous stock data for each stock mentioned in ticker.csv file and saves it as csv file after formatting them to panda data frame.
It will not create csv files if data is missing for any stock.
3. On 1st, and 16th of month, the models for each stock get trained with new data which is a time consuming task. Each model creation takes approximately 10 minutes to save.
4. When User selects a date and stock same on the web browser, the streamlit application NextDayStockPredict.py reloads relative model as per the stock and predict the data.


## Architecture



## Monitoring



## Notes

Please read  **Stock Market Prediction Application User Guide.pdf**
for further information.


