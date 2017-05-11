import requests
from bs4 import BeautifulSoup
import pandas as pd   #用來做資料分析的工具，
import time
url = 'http://www.tse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'

def parseTSE(year, month, no):
    str(year)
    str(month)
    str(no)

    payload = {
        'myyear':year,
        'mmon':month,
        'STK_NO':no,
        'login_btn': '%ACd%B8%DF'
        #'query_btn':'%E6%9F%A5%E8%A9%A2'
    }

    headers ={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    }

    res = requests.post(url, headers=headers, data=payload)
    time.sleep(3)
    #data = res.text.encode('latin1').decode('big5')
    print(res.text)
    #print(data)

parseTSE(2015, 12, 2317)
#soup =
