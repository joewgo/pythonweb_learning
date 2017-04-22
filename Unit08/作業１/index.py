#print('hello youtube!!')
from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
app = Flask(__name__)

@app.route('/')
def index():
    filename = request.args.get('filename')
    filename1 = request.args.get('filename1')
    return render_template('index.html', filename=filename,filename1=filename1)


@app.route('/submit', methods=['POST'])
def post_submit():
    yt = YouTube()
    url = request.form.get('url')
    yt.url = url
    video = yt.get('mp4', '720p')
    video.download('./')
    filename = yt.filename
    print(yt)
    print(yt.filename)
    return redirect(url_for('index', filename=filename))

@app.route('/submit1', methods=['POST'])
def post_submit1():
    yt = YouTube()
    url = request.form.get('url1')
    yt.url = url
    video = yt.get('mp4', '720p')
    video.download('./')
    filename1 = yt.filename
    print(yt)
    print(yt.filename)
    return redirect(url_for('index', filename1=filename1))

if __name__ == '__main__':
    app.run(debug=True)
