On google deep learning image instance to setup environment:
-----------------------------------------------------------

git clone https://github.com/moumita-das-7019/StockPredict.git

cd StockPredict

pip install streamlit

python3 -m pip install -r requirements.txt --user

streamlit run StockPredict.py

#Run the scripts manually if not automated in server
python3 ticker.py #To get all tickers of Indian Stock Exchange available
python3 SaveData.py #To get all the stock price data of individual stocks
python3 CreateModel.py #To save all the models of Individual stock

#You need to create API key to get stock data from https://marketstack.com/quickstart


These are the Libraries needed:
pandas
numpy
sklearn
streamlit
scipy
keras
math
requests
datetime
tensorflow


Other softwares:
streamlit
git
tmux
python3
pip
sudo access
tensorflow

