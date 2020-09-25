import time

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json
import math
import keras
import datetime
from datetime import date
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM


def createModel(stock):
    new = pd.read_csv('/home/moumita_das2820/StockPredict/data/'+stock+'.csv')
    #Create a new dataframe with only the 'Close' column
    data = new.filter(['close'])
    #Converting the dataframe to a numpy array
    dataset = data.values
    #Get /Compute the number of rows to train the model on
    training_data_len = math.ceil( len(dataset) *.8) 
    #Scale the all of the data to be values between 0 and 1 
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    scaled_data = scaler.fit_transform(dataset)
    #Create the scaled training data set 
    train_data = scaled_data[0:training_data_len  , : ]
    #Split the data into x_train and y_train data sets
    x_train=[]
    y_train = []
    for i in range(60,len(train_data)):
            x_train.append(train_data[i-60:i,0])
            y_train.append(train_data[i,0])
    #Convert x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)
    #Reshape the data into the shape accepted by the LSTM
    x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    #Build the LSTM network model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    #Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    #Train the model
    model.fit(x_train, y_train, batch_size=2, epochs=20)
    model.save('/home/moumita_das2820/StockPredict/data/'+stock+'_model')

tickers = pd.read_csv('/home/moumita_das2820/StockPredict/data/ticker.csv')
#Save each model
for stock in tickers['symbol']:
    print(stock)
    createModel(stock)

