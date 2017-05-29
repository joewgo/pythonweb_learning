import requests
import json
import matplotlib.pyplot as plt

url = 'http://data.fda.gov.tw/cacheData/35_3.json'

res = requests.get(url)
#print(res.text)
items = json.loads(res.text)

data = [0, 0, 0]
for item in items:
    #print(item)
    #if item[6]['負責人性別'] == '男':
    #    data[0] += 1
    #elif item[6]['負責人性別'] == '女':
    #    data[1] += 1
    if item[8]['是否為健保特約藥局'] == 'Y':
        data[0] += 1
    elif item[8]['是否為健保特約藥局'] == 'N':
        data[1] += 1
    elif item[8]['是否為健保特約藥局'] == '':
        data[2] += 1
lables = ['Y','N','nothing']

plt.pie(data, labels=lables)
plt.show()
