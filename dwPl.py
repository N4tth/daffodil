
import os
from pytube import YouTube
from pytube.contrib.playlist import Playlist
from moviepy.editor import AudioFileClip
from pathlib import Path

wayPATH = str(Path.home()/"Downloads")

def mp3(vidPath, mp3Path):
    audioClip = AudioFileClip(vidPath)
    audioClip.write_audiofile(mp3Path)
    audioClip.close()
    os.remove(vidPath)

def download(url, way):
    yt = Youtube(url)
    video = yt.streams.filter(onlyAudio=True).first()
    outFile = video.download(outputPath=way)
    base, ext = os.path.splitext(outFile)
    newArchive = base + '.mp3'
    mp3(outFile,newArchive)
    print(f"Done! {newArchive}")

def handlePlaylist(url,way):
    playlist = Playlist(url)
    print(f"Downloading {playlist.title} ...")
    for video_url in playlist.video_urls:
        print(f"{video_url}")
        download(video_url, way)
    print("Done all!")

def downloadYT(url, way = wayPATH):
    if 'playlist' in url:
        handlePlaylist(url, way)
    else: 
        download(url, way)