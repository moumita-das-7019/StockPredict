import streamlit as st
import os
from PIL import Image
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json
import math
import pickle
import joblib
import keras
import datetime
from requests.exceptions import HTTPError
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
#from datetime import datetime
from datetime import date
# Creating the Titles and Image
st.title("Indian Stock Market Prediction")
st.header("Finding a probable stock price using Machine Learning")
st.write("Please choose a stock and date to get your stock price:")
image = Image.open('StockMarket.jpg')
st.image(image, use_column_width=True)
st.write("Image Courtesy: https://www.clickastro.com/ogimages/indian-stock-market-predictions.jpg")
df = pd.read_csv("/home/moumita_das2820/StockPredict/data/ticker.csv")
"The Stock price prediction available at our website for these Indain stocks:"
df
option = st.selectbox('Which Stock do you like best?',df['symbol'])
'You selected: ', option
#UserDate=st.date_input('Please choose a date within next 30 days:', datetime.date(2020, 10, 1))
#'You have chosen: ', UserDate

#Choose model for prediction

def PredictStock(stock):
    #Load model
    model = keras.models.load_model('/home/moumita_das2820/StockPredict/models/'+stock+'_model')
    #Load datafile
    df1 = pd.read_csv('/home/moumita_das2820/StockPredict/data/'+stock+'.csv')
   #Create a new dataframe with only the 'Close' column
    data = df1.filter(['close'])
    #Converting the dataframe to a numpy array
    dataset = data.values
    #Get /Compute the number of rows to train the model on
    training_data_len = math.ceil( len(dataset) *.8) 
    #Scale the all of the data to be values between 0 and 1 
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    scaled_data = scaler.fit_transform(dataset)
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
    predictions = model.predict(x_test) 
    predictions = scaler.inverse_transform(predictions)#Undo scaling
    #Calculate/Get the value of RMSE
    rmse=np.sqrt(np.mean(((predictions- y_test)**2)))
    'RMSE measures the accuracy of AI prediction, not to worry if you do not undetstand. RMSE:', rmse
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    valid['Date'] = df1['date']
    valid = valid.set_index('Date')
    return valid


#Call funnction to predict values with user input
FutureValues = PredictStock(option)
TodayValue = FutureValues["Predictions"].iloc[-1]
"The closing price based on AI prediction today is:", TodayValue, "."
"Here is the actual closing price and AI Predicted closing value of this stock for your comparison of last 60 days:"
FutureValues
"Please note: Stock market is unpredictable, and these data is only for reference. Please use your decision making when looking to invest."

