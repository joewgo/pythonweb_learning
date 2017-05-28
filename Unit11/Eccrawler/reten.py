import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=2'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}

res = requests.get(url,headers=headers)
#soup = BeautifulSoup(res.text.encode('latin1').decode('utf8'), 'html.parser')

#result = soup.select('.results-listing')
#print(result)

browser = webdriver.PhantomJS(executable_path='./phantomjs')
browser.get(url)
#print(browser.page_source)

soup = BeautifulSoup(browser.page_source, 'html.parser')
result = soup.select('.results-listing')[0]

items = result.select('.media-body')

data = []

for item in items:
    print(item.select('.item-name-text')[0].text)
    print(item.select('.item-name-anchor')[0]['href'])
    print(item.select('.rt-text-price')[0].text)

    data.append({
        'name':item.select('.item-name-text')[0].text,
        'link':item.select('.item-name-anchor')[0]['href'],
        'price':item.select('.rt-text-price')[0].text
    })

with open('./ruten.txt','w') as f:
    f.write(str(data))
