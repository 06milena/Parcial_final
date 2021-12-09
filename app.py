from flask import Flask, render_template, request, redirect, flash, jsonify
from controllers import users
import youtube_dl

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.get('/')
def youtube():
    return render_template('youtube.html')

@app.get("/info-video")
def infoVideo():
    url = request.args.get("url")
    
    videoId = url.replace('https://www.youtube.com/watch?v=', '')

    return render_template('info_video.html', videoId = videoId, url = url)

@app.get('/descargar-video')
def descargarVideo():
    url = request.args.get("url")

    videoId = url.replace('https://www.youtube.com/watch?v=', '')

    links = [
        url
    ]

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '190',
        }],
        'outtmpl': './static/' + videoId + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

    return jsonify({
        'url': 'http://localhost:5000/static/'+ videoId + '.mp3'
    })

app.run(debug=True)