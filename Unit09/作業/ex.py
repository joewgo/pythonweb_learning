import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
headers ={
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}
res = requests.get('https://www.ptt.cc/man/Beauty/DF7B/D111/M.1400913738.A.BD8.html', headers=headers)

#https://www.ptt.cc/man/Beauty/DF7B/D111/M.1400913738.A.BD8.html


#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
images = soup.select('a[href^=http://i.imgur]')
print(images)
for image in images:
    print(image['href'])
    filename = image['href'].split('/')[3]
    #print (filename)
    img = urlopen(image['href'])
    #w:寫入　,b:binary (二進位檔案)
    with open('./images/' + str(filename),'wb') as f:
        f.write(img.read())
