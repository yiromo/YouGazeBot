from pytubefix import YouTube
import logging

def download_video(link: str):
    video = YouTube(link)
    print(video.title)
    video = video.streams.get_highest_resolution()
    video.download()


link = "https://www.youtube.com/watch?v=Py_8GuYC4X4"
download_video(link)
