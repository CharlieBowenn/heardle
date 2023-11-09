#Access Spotify through API
import tekore as tk
import requests
import time
import io
from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio
import random

def get_access_token(id, secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": id,
        "client_secret": secret
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code==200:
        access_token = response.json().get("access_token")
        return access_token
    else:
        print(response.content)
        raise Exception("Failed to retrieve access token")

def get_artist_top_tracks(artist_name, numSongs, access_token):
    url = f"https://api.spotify.com/v1/search"
    params = {
        "q": f"artist:{artist_name}",
        "type": "track",
        "limit": numSongs
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code==200:
        data = response.json()
        print(data)
        # print(data["tracks"]["items"][0])
        top_tracks = list()
        for x in range(numSongs):
            top_tracks.append(data["tracks"]["items"][x].get("name"))
        # print(f"top_tracks: {top_tracks}")
        # print(data["tracks"]["items"][0].get('preview_url'))
        # print(data["tracks"]["items"][0].get('track_url'))
        return data["tracks"]["items"][0].get('preview_url')
    else:
        raise Exception("Failed to get artist's top track")
    
def random_playlist_song(playlist_name, numSongs, access_token):
    spotify = tk.Spotify(access_token)
    url = f"https://api.spotify.com/v1/search"
    params = {
        "q": playlist_name,
        "type": "playlist",
        "limit": numSongs
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code==200:

        responseID = response.json()
        first_items = spotify.playlist_items(responseID['playlists']['items'][0].get('id'))
        all_items = spotify.all_items(first_items)
        available = {}
        
        for x in spotify.all_items(first_items):
            if x.track.preview_url:
                available[x.track.name] = x.track.preview_url
        choice = random.choice(list(available.keys()))
        print(choice)
        return available[choice], choice
    else:
        raise Exception("Failed to get artist's top track")    
    # response = requests.get(responseID['playlists']['items'][0].get('href')+'/tracks', headers=headers)
    # print(response)
    # if response.status_code==200:
    #     data = response.json()
    #     # print('data')
    #     print(data)
    #     # print('data[items]')
    #     # print(data['items'])
    #     available = {}
    #     for x in data['items']:
    #         if x['track']['preview_url'] is not None:
    #             available[x['track']['name']] = x['track']['preview_url']
    #     print(len(data['items']))
    #     print(len(available.keys()))
    

    # # print(responseID['playlists']['items'][0].get('id'))
    # print('responseID')
    # print(responseID)
    # print('-----------------------------------------------------------------------------------')
    # print('responseID[playlists][items]')
    # print(responseID['playlists']['items'][0].get('href'))
    # print('-----------------------------------------------------------------------------------')
    # for x in responseID['playlists']['items']:
    #     print(x)
    #     print('======================')



    # print(responseID['playlists']['items'][0].get('href')+'/tracks')
    
    



        # for x in data['items']:
        #     print('000000000000000000000000000000000')
        #     print(x['track']['name'])
        # found = False
        # while not found:
        #     choice = random.choice(data['items'])
        #     if choice['track']['preview_url'] is not None:
        #         return choice['track']['preview_url']
    
def setup(choice):
    id = "fad55531967b4fdba101b451a9c0b20b"
    secret = open("spotifySecret.txt", "r").read()
    token = tk.request_client_token(id, secret)
    playlistChoices = {
        'Rock': 'Rock Classics',
        'Rap': 'UK RAP BANGERS'
    }
    topURL, name = random_playlist_song(playlistChoices[choice], 1, token)
    response = requests.get(topURL)
    if response.status_code==200:
        audio = response.content
        song = AudioSegment.from_file(io.BytesIO(audio), format='mp3')
        return song, name
    else:
        raise Exception('Failed to get song')
    
    

# if __name__ == "__main__":
#     id = "fad55531967b4fdba101b451a9c0b20b"
#     secret = open("spotifySecret.txt", "r").read()
#     token = tk.request_client_token(id, secret)
#     # token = get_access_token(id, secret)
#     # artist = input("Enter an artist: ")
#     # topURL = get_artist_top_tracks(artist, 1, token)
#     topURL, name = random_playlist_song('Rock Classics', 1, token)
#     response=requests.get(topURL)
#     if response.status_code==200:
#         audio = response.content
#         song = AudioSegment.from_file(io.BytesIO(audio), format='mp3')
#         playback = _play_with_simpleaudio(song)
#         time.sleep(10)
#         playback.stop()
#     else:
#         raise Exception("Failed to get song")