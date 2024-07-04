
import os
from pytube import YouTube
from pytube.contrib.playlist import Playlist
from moviepy.editor import AudioFileClip
from pathlib import Path

def getPATH():
    downloadPATH = Path.home() / "Downloads"
    if not downloadPATH.exists():
        print(f"Lol {downloadPATH} doesn't exists")
        downloadPATH.mkdir(parents=True, exist_ok=True)
    return str(downloadPATH)

wayPATH = getPATH()

def mp3(vidPath, mp3Path):
    try:
        audioClip = AudioFileClip(vidPath)
        audioClip.write_audiofile(mp3Path)
        audioClip.close()
        os.remove(vidPath)
        print(f"{vidPath} to {mp3Path} converted")
    except Exception as e:
        print(f"Error converting {vidPath} to MP3: {e}")

def download(url, way):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        outFile = video.download(way)
        base, ext = os.path.splitext(outFile)
        newArchive = base + '.mp3'
        mp3(outFile,newArchive)
        print(f"Done! {newArchive}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def handlePlaylist(url,way):
    try:
        playlist = Playlist(url)
        print(f"Downloading {playlist.title} ...")
        for video_url in playlist.video_urls:
            print(f"{video_url}")
            download(video_url, way)
        print("Done all!")
    except Exception as e:
        print(f"Error handling playlist {url}: {e}")

def downloadYT(url, way = wayPATH):
    if 'playlist' in url:
        handlePlaylist(url, way)
    else: 
        download(url, way)