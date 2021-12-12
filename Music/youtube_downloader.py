from __future__ import unicode_literals
import youtube_dl
import os
from bs4 import BeautifulSoup
import requests
import normalized_text

url_playlist = input("URL de la playlist o la cancion: ")
url_contents = requests.get(url_playlist)

soup = BeautifulSoup(url_contents.text, 'lxml')
div_bs4 = soup.title

title = str(div_bs4)
words = ['<title>','</title>','YouTube','-',' ']

for x in words:
    title = title.replace(x,"")
print(title)
try:
    os.mkdir("Downloads")
except:
    pass
os.chdir("Downloads")
try:
    os.mkdir(title)
except:
    pass

os.chdir(title)

ydl_opts = {
    'format': 'bestaudio/best',
    'playlist-end': 2,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
i = 0
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url_playlist])

files = os.listdir()

normalized_text.normalize(os.getcwd())

    