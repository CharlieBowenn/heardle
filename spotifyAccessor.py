#Access Spotify through API
import requests

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
        top_tracks = list()
        for x in range(numSongs):
            top_tracks.append(data["tracks"]["items"][x].get("name"))
        print(f"top_tracks: {top_tracks}")
    else:
        raise Exception("Failed to get artist's top track")

if __name__ == "__main__":
    id = "fad55531967b4fdba101b451a9c0b20b"
    secret = open("spotifySecret.txt", "r").read()
    token = get_access_token(id, secret)
    artist = input("Enter an artist: ")
    get_artist_top_tracks(artist, 5, token)