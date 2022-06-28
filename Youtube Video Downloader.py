from asyncio import streams
from pytube import YouTube
link = input("Enter the URL link here: ")
youtube_1 = YouTube(link)
videos = youtube_1.streams.all()
print(youtube_1.title)
print(youtube_1.thumbnail_url)
vid = list(enumerate(videos))
for i in vid:
    print(i)
    print()
    strm = int(input("Enter 0 to Download the File: "))
    videos[strm].download()
    print("Successfully Downloaded")
