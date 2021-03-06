# -*- coding: utf-8 -*-
"""Using AI to split songs to multiple sources

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8JNIN-gDVgCUl61C-ua3TlaEe9y24cM

<figure class="image">
  <img src="https://sigsep.github.io/assets/img/musheader.41c6bf29.png" alt="Dataset illustration">
  <figcaption>Source: MUSDB18 dataset home page (Link in course resources)</figcaption>
</figure>




## Installing dependencies for the project
"""

!apt install ffmpeg # A complete, cross-platform solution to record, convert and stream audio and video
!pip install librosa # LibROSA is a python package for music and audio analysis.
!pip install youtube-dl # Helper library to download any youtoube video to MP3/WAV format

pip install spleeter # Library that splits audio to multiple channels

"""## Import dependencies"""

import librosa
import youtube_dl

# Jupyter Notebook visualization functions
from IPython.display import Audio, display
from IPython.display import HTML

"""## Dewnload video from youtube 

**Disclaimer: I don’t own the rights to songs mentioned in this course, the copyrights are of the official music creators and labels.**
"""

url = "BPwZaQfoIbU" #@param {type:"string"}
embed_url = "https://www.youtube.com/embed/%s?rel=0&amp;controls=0&amp;showinfo=0" % (url)
HTML('<iframe width="560" height="315" src=' + embed_url + 'frameborder="0" allowfullscreen></iframe>')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'example_song.wav'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    status = ydl.download([url])

audio, rate = librosa.load('example_song.wav', sr=44100, mono=False)

display(Audio(audio[:, 0*rate:40*rate], rate=rate))

audio.shape

audio

"""## Split songs to separate channels using AI


<figure class="image">
  <img src="https://miro.medium.com/max/2824/1*f7YOaE4TWubwaFF7Z1fzNw.png" alt="Dataset illustration">
  <figcaption>Source: UNet — Line by Line Explanation (Link in course resources)</figcaption>
</figure>
"""

!spleeter separate -h

!spleeter separate -i example_song.mp3 -p spleeter:4stems -o output

"""## Let's use Audacity to play different parts of the song"""