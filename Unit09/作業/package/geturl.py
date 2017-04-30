
#從文字文件取得網址後，進行回傳
def geturl1(text):
    with open(text,'r') as f:
        result = f.read().split()

    return result
