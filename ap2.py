from flask import Flask
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrap_data():
    resp= requests.get("https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03")
    soup= BeautifulSoup(resp.content)
    div = soup.find("div", attrs={"id":"nsecp"})
    return div.text

def send_alert():
    response = {"value1": stock_price, "value2": "", "value3": ""}
    requests.post("https://maker.ifttt.com/trigger/alert/with/key/nuj_TrWewItf0im7cyQs2EnLBEti3nncNlQ6R4wq-zz",
                  data=response)



@app.route('/', methods=["GET",'POST'])
def index():
    global stock_price
    stock_price = scrap_data()
    threshold = 270
    if float(stock_price)>threshold:
        send_alert()
    return stock_price

if __name__ == '__main__':
    app.run(host='0.0.0.0')