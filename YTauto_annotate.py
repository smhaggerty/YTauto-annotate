
from __future__ import unicode_literals
import youtube_dl

def download_YT_audio_as_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        print('Enter the download link to extract audio:  ')
        ydl.download([url])

print('Enter the link to download audio from:')
download_YT_audio_as_mp3(input())
