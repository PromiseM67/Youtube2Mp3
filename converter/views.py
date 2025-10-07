from django.shortcuts import render
import os
import yt_dlp
from django.http import FileResponse, HttpResponse

def home(request):
    return HttpResponse('Checking if it is linked')
# Create your views here.

def index(request):
    if request.method == 'POST': # if the request is a POST request, It is a submission from the user and it requires the website to fetch something
        url = request.POST.get('url') # the user sends a request, which is the url for the youtube video

        # adds the following configurations to the youtube to mp3
        ydl_opts ={
            'format':'bestaudio/best',
            'outtmpl':'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192'
            }],
            'ffmpeg_location':"C:\\Users\\promi\\Downloads\\ffmpeg-8.0-essentials_build\\ffmpeg-8.0-essentials_build\\bin\\ffmpeg.exe",
        }

        # creates an object with the configurations made above 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True) # downloads the video
            filename = ydl.prepare_filename(info).rsplit('.',1)[0]+'.mp3'

            return FileResponse(open(filename, 'rb'), as_attachment=True) # returns the file as a download to the user, as attachment downloads it instead of opening it
        # rb stands for read as binary which is needed for audio and video files.

    return render(request, 'index.html')


