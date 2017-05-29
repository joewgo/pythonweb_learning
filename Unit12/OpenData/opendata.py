import requests
import json
import matplotlib.pyplot as plt

url = 'http://data.fda.gov.tw/cacheData/35_3.json'

res = requests.get(url)
#print(res.text)
items = json.loads(res.text)

data = [0, 0]
for item in items:
    #print(item)
    if item[6]['負責人性別'] == '男':
        data[0] += 1
    elif item[6]['負責人性別'] == '女':
        data[1] += 1
lables = ['man', 'woman']

plt.pie(data, labels=lables)
plt.show()
