#!/bin/python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json
import math
import keras

from datetime import datetime
from requests.exceptions import HTTPError
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, LSTM

#Get data
try:
    response = requests.get('http://api.marketstack.com/v1/eod?access_key=7a247f5ee1c585714c83b74587866efb&symbols=TCS.XNSE&%20date_from=2000-01-01&limit=1000')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

#Prepare data as pd dataframe
df = pd.DataFrame(jsonResponse['data']) 
df1 = df[['symbol', 'open', 'close', 'adj_close', 'date']]
df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d''T''%H:%M:%S+%f')
df1.set_index('date', inplace = True)
df1.sort_values(by='date', ascending=1, inplace=True)

#Create a new dataframe with only the 'Close' column
data = df1.filter(['close'])
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

model.save('StockModelTCS')

Oldmodel = keras.models.load_model('./StockModelTCS')

#Test data set
test_data = scaled_data[training_data_len - 60: , : ]
#Create the x_test and y_test data sets
x_test = []
y_test =  dataset[training_data_len : , : ] #Get all of the rows from index 1603 to the rest and all of the columns (in this case it's only column 'Close'), so 2003 - 1603 = 400 rows of data
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i,0])

#Convert x_test to a numpy array 
x_test = np.array(x_test)

#Reshape the data into the shape accepted by the LSTM
x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))

#Getting the models predicted price values
predictions = Oldmodel.predict(x_test) 
predictions = scaler.inverse_transform(predictions)#Undo scaling

#Calculate/Get the value of RMSE
rmse=np.sqrt(np.mean(((predictions- y_test)**2)))
rmse

train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

#Show the valid and predicted prices
valid

userDate = '2020-07-21'
if userDate in valid.index:
    print(valid._get_value(userDate, 'Predictions'))
else:
    print("Sorry we dont have the data")

