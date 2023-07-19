import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
import subprocess
from moviepy.editor import *
from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog

playlist_url = 'coloque aqui o link da playlist'

client_id = "coloque aqui o seu client id"
client_secret = "coloque aqui o seu client secret"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

root = tk.Tk()
root.withdraw()
download_dir = filedialog.askdirectory()

def download_by_link(query, youtube_link):
    try:
        command = 'ytmdl --url ' + '\"' + youtube_link + '\"' + ' --skip-meta' + ' -o' + ' \"' + download_dir + '\"'
        subprocess.call(command, shell=True)

        name_yt = YouTube(youtube_link).title
        for file in os.listdir(download_dir):
            if file.endswith('.mp3'):
                if name_yt == file.replace('.mp3', ''):
                    os.rename(os.path.join(download_dir, file), os.path.join(download_dir, query + '.mp3'))
    except:
        print("Error")

def search_youtube_link(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    url = 'https://www.youtube.com' + results[0]['url_suffix']
    return url

playlist = sp.playlist(playlist_url)

tracks = playlist['tracks']

while True:
    for track in tracks['items']:
        song_name = track['track']['name']
        artists = [artist['name'] for artist in track['track']['artists']]
        query = f"{song_name} - {', '.join(artists)} - Extended mix audio"
        print(query)
        full_name = f"{song_name} - {', '.join(artists)}"

        youtube_link = search_youtube_link(query)
        download_by_link(full_name, youtube_link)

    if tracks['next']:
        tracks = sp.next(tracks)
    else:
        break