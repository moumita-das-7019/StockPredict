import streamlit as st
import pandas as pd
import os
from PIL import Image
import datetime
import numpy as np # linear algebra
import requests
import json
import math
import keras
from datetime import date
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, LSTM

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
UserDate=st.date_input('Please choose a date within next 30 days:', datetime.date(2020, 10, 1))
'You have chosen: ', UserDate


#Choose model for prediction

def PredictStock(stock, UserDate):
    #Load model
    model = keras.models.load_model('/home/moumita_das2820/StockPredict/data/'+stock+'_model')
    #Load datafile
    df1 = pd.read_csv('/home/moumita_das2820/StockPredict/data/'+stock+'.csv')
   #Create a new dataframe with only the 'Close' column
    data = df1.filter(['close'])
    #Converting the dataframe to a numpy array
    dataset = data.values
    #Get /Compute the number of rows to train the model on
    training_data_len = math.ceil( len(dataset) *.8) 
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

    #Calculate value for given date
    today = date.today()
    PreviousDate = datetime.date.today() - (userDate - today)
    #Function to calculate prediction and close value of today, previous data
    def PredValues(date):
            date1 = date.strftime("%Y-%m-%d")
            while date1 not in valid.index:
                  date = date - datetime.timedelta(days=1)
                  date1 = date.strftime("%Y-%m-%d")
            if date1 in valid.index:
                   datePrediction = valid._get_value(date1, 'Predictions')
                   dateClose = valid._get_value(date1, 'close')
            dateValues = [ datePrediction, dateClose ]
            return dateValues
    TodayValues = PredValues(today)
    PastValues = PredValues(PreviousDate)
    difference = []
    zip_object = zip(TodayValues, PastValues)
    for list1_i, list2_i in zip_object:
            difference.append(list1_i-list2_i)
    FutureValues = []
    zip_object = zip(TodayValues, difference)
    for list1_i, list2_i in zip_object:
            FutureValues.append(list1_i+list2_i)

    FutureValues = []
    zip_object = zip(TodayValues, difference)
    for list1_i, list2_i in zip_object:
        FutureValues.append(list1_i+list2_i)
    return FutureValues


#Call funnction to predict values with user input
FutureValues = PredictStock(option, UserDate)
"The closing price based on AI prediction is", FutureValues[0], "and based on past closing values is",FutureValues[1], "."
'''
imaginary_stock = {
    "23-09-2020" : "56",
    "24-09-2020" : "60",
    "25-09-2020" : "100"
    }
if UserDate in imaginary_stock:
        stockValue = imaginary_stock[UserDate]
        st.write("Predicted stock price for", UserDate, " is ", stockValue)
'''
st.write("""
Please note: Stock market is unpredictable, and these data is only for reference. Please use your decision making when looking to invest.
""")
