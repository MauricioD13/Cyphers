from __future__ import unicode_literals
import youtube_dl
import os
from pydub import AudioSegment


try:
    os.mkdir('Downloads')
except:
    pass

os.chdir('Downloads')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
    ydl.download(['https://www.youtube.com/playlist?list=PLrxmU3_Xf6TIP2apRm5s3b21eVt8Iwo95'])

files = os.listdir()
tittle = []

for file in files:
    tittle = file.split('.')
    if(tittle[1]=='mp4'):
        tittle = tittle[0].split('-')
    new_tittle = tittle[0]+'_'+tittle[1]+'.mp4'
    new_tittle = new_tittle.replace(' ','_')

    os.rename(file,new_tittle)
    new_tittle_mp3 = tittle[0]+'_'+tittle[1]+'.mp3'
    new_tittle_mp3 = new_tittle_mp3.replace(' ','_')
    print(f'mp4 {new_tittle} mp3 {new_tittle_mp3}')
    os.system('ffmpeg -i '+new_tittle+' -vn -ar 44100 -ac 2 -b:a 192k '+new_tittle_mp3)

    

    