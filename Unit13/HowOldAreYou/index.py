import cv2
from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    filename = request.args.get('filename')
    result = request.args.get('result')
    return render_template('index.html', filename=filename, result=result)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['img'] #對應到index.html中的img<input type="file" name="img" value="">

        file.save('./' + file.filename)

        cascPath = 'haarcascade_frontalface_default.xml' #特徵值檔案路徑

        faceCascade = cv2.CascadeClassifier(cascPath)

        image = cv2.imread(file.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #將圖從ＢＧＲ轉成gray(灰階)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2, #通常這值給１，但我們給1.2 (依據不同大小去對圖片進行掃瞄特徵的比對)
            minNeighbors=5, #控製檢驗的誤差參數，設５個區塊, 特徵比對都正確則判斷有人臉(預設值為３)
            minSize=(30, 30), #每次去辨識的區塊，它的大小是怎麼樣
            flags= cv2.CASCADE_SCALE_IMAGE #檢測的一些模式
        )
        #rectangle　矩形的意思
        for (x, y, w, h) in faces:
            age = random.randint(18, 30) #年齡設在１８~３０歲
            #矩形的寬度設為２, 實心則改負值
            cv2.rectangle(image, (x + 3, y - 15), (x + 50, y - 50), (200, 187, -1), -1)
            #最後項目為文字粗細:２
            cv2.putText(image, str(age), (x + 5, y - 20),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 187), 2)
            #矩形的寬度設為２
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite('./static/images/' + file.filename, image)
        newImage = './static/images/' + file.filename

    return redirect(url_for('index', filename=newImage, result=len(faces)))#最後確認是否有辨識成功。
    #若成功會是一個串列result=len(faces)
if __name__ == '__main__':
    app.run()
