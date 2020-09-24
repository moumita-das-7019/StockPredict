#Install required softwares

sudo yum install python36 git -y

pip install streamlit

sudo pip install --upgrade pip

git clone https://github.com/moumita-das-7019/StockPredict.git

cd StockPredict

python36 -m pip install -r requirements.txt --user

streamlit run StockPredict.py
