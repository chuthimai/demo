from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

endpoint = "https://api.spotify.com/v1/artists/"

CLIENT_ID = os.environ.get("ClientID")
CLIENT_SECRET = os.environ.get("ClientSecret")
TOKEN = os.environ.get("TOKEN")
OAUTH = f"Bearer ${TOKEN}"
USER_ID = os.environ.get("ID")
URI = f"spotify:user:{USER_ID}"

date = input("Which year do you want to travel to? Type the date in this format yyyy-mm-dd: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

sp = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

playlist = sp.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public=False)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

soup = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
list_song = [song.text.strip() for song in soup]
print(list_song)


song_uris = []
for song in list_song:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)



