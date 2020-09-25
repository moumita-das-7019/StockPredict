import streamlit as st
import pandas as pd
import os
from PIL import Image
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


UserDate = st.text_input("Please enter a date:")
'You have chosen: ', UserDate

imaginary_stock = {
    "23-09-2020" : "56",
    "24-09-2020" : "60",
    "25-09-2020" : "100"
    }
if UserDate in imaginary_stock:
        stockValue = imaginary_stock[UserDate]
        st.write("Predicted stock price for", UserDate, " is ", stockValue)

st.write("""
Please note: Stock market is unpredictable, and these data is only for reference. Please use your decision making when looking to invest.
""")