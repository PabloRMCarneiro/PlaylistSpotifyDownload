import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
import subprocess
from moviepy.editor import *
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


playlist_url = "PLAYLIST_URL" # coloque aqui a url da sua playlist

client_id = "CLIENT_ID" # coloque aqui eu client_id  do seu app do spotify
client_secret = "CLIENT_SECRET" # coloque aqui eu client_secret  do seu app do spotify

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist = sp.playlist(playlist_url)
tracks = playlist['tracks']

root = tk.Tk()
root.withdraw()
download_dir = filedialog.askdirectory()

def youtube_search_link(search_song_title):
    # dado o nome da música retornar o primeiro link do youtube
    try:
        results = YoutubeSearch(search_song_title, max_results=1).to_dict()
        link = 'https://www.youtube.com' + results[0]['url_suffix']
        return link
    except Exception as e:
        print(e)


def download_by_link(link_song, id_song):
    try:
        command = 'ytmdl  --url ' + '\"' + link_song + '\"' + ' --quiet' + ' -o ' + '\"' + download_dir + '\"' + ' --spotify-id ' + ' \"' + id_song + '\"'
        subprocess.call(command, shell=True)
    except Exception as e:
        print(e)

while True:
    for track in tracks['items']:
        id_song = track['track']['id']
        song_name = track['track']['name']
        artists = [artist['name'] for artist in track['track']['artists']]
        search_song_title = f"{song_name} - {', '.join(artists)} - Original Extended Mix" # retire o "- Original Extended Mix" se quiser a música original

        download_by_link(youtube_search_link(search_song_title), id_song)
    if tracks['next']:
        tracks = sp.next(tracks)
    else:
        break
