import requests
from bs4 import BeautifulSoup
import pandas as pd   #用來做資料分析的工具，
import time
url = 'http://www.tse.com.tw/zh/page/trading/exchange/BWIBBU.html'

def parseTSE(year, month, no):
    year = str(year)
    month = str(month)
    no = str(no)

    payload ={
        'query_year':year,
        'query_month':month,
        'CO_ID':no,
        'query-button':'查詢'
    }
    headers ={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    }
    '''
    payload = {
        'myyear':year,
        'mmon':month,
        'STK_NO':no,
        'login_btn': '%ACd%B8%DF'
        #'query_btn':'%E6%9F%A5%E8%A9%A2'
    }
    '''
    res = requests.post(url, headers=headers, data=payload)
    #time.sleep(3)
    #data = res.text.encode('latin1').decode('big5')
    #print(data)
    #soup = BeautifulSoup(data,'html.parser')
    #print(res.text)
    data = res.text
    soup = BeautifulSoup(data,'html.parser')
    content = soup.select('table')[0]   #這行因為網站改版，所以改抓table

    with open('./' + year + month + '_tse_' + no + '.html', 'w') as f:
        f.write(str(content))

    table = pd.read_html('./' + year + month + '_tse_' + no + '.html',encoding='utf-8')[0]#,encoding='utf-8'
    #table = table.drop(table.index[0:2])#老師有發佈新版仍有這行，有可能是Debian造成//因為爬文的網站改版，這行可能不需要了。
    #print(table)
    #print(content)
    print(table.to_csv(header=False, index=False))

    with open('./' + year + '_tse_' + no + '.csv', 'a') as f:
        f.write(str(table.to_csv(header=False, index=False)))


for m in range(1,13):
    parseTSE(2015, m, 2317)
    time.sleep(5)

#soup =
