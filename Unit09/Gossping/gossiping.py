# https://www.ptt.cc/ask/over18
# /bbs/Gossiping/index.html
# https://www.ptt.cc/bbs/Gossiping/index.html

import requests
from bs4 import BeautifulSoup

payload ={
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

headers ={
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}

rs = requests.Session()

rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)

#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent') # class用　. 若 id 則用　#
#print(items)
for item in items:
    #print('日期{}'.format(item.select('.data')[0].text))
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)
