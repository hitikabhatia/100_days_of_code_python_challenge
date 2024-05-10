import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import re

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

#Todo 2: Access Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://www.example.com/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               username="YOUR_USERNAME",
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]

year = input("Which year do go want to travel to ? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(billboard_url)
billboard_page = response.text

#Todo 1: scrape the top 100 song titles on that date into a Python List.
billboard_page_soup = BeautifulSoup(markup=billboard_page, parser="lxml.parser", features="lxml")
song_elements = billboard_page_soup.select(selector="li h3", id="title-of-a-story")

#Getting all titles of top-100 songs in a list
song_titles = [song_elements[song_number].getText().strip() for song_number in range(0, 100)]
# print(song_titles)

#Todo 3: Getting all artist name of the top-100 songs in a list
name_elements = billboard_page_soup.select(selector="html body div main div div div div div div div ul li ul li span")

artist_names = [each_element.getText().strip() for each_element in name_elements if (each_element.getText().isnumeric() == False)]

unwanted_elements = [each_element for each_element in artist_names if re.match(pattern=r"[0-9]",string=each_element)]

for each_un in unwanted_elements:
    if each_un in artist_names:
        artist_names.remove(each_un)

artists = [each_name for each_name in artist_names if each_name != "-"]
#print(artists)         #This gives a list of artists for all the top 100 songs in order from top to bottom
#print(len(artists))

#Todo 4: Search for all the songs from spotify using song-title and artist-name and add the song-uris to a new list
spotify_song_uris = []

for track_number in range(0, 100):
    song_track = song_titles[track_number]
    song_artist = artists[track_number]

    urn = f"artist :  {song_artist} track: {song_track} year: {year[0:4]}"
    song = sp.search(q=urn, limit=1, offset=0, type="track")
    try:
        track_uri = song["tracks"]["items"][0]["uri"]
        spotify_song_uris.append(track_uri)
    except IndexError:
        print(f"This song {song_track} by {song_artist} does not exist in Spotify. Skipped.")

    # print("-"*50,f"Track Number {track_number+1} from the top-100 billboard list","-"*50, sep=" ")
    # pprint.pprint(song)
    # print("#"*200)

# for each_song_uri in spotify_song_uris:
#     print(each_song_uri, type(each_song_uri))

#Todo 5: Create a spotify playlist
spotify_playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False, description=f"This playlist contains top 100 billboard songs from date-{year}.")
sp.playlist_add_items(playlist_id=spotify_playlist["id"], items=spotify_song_uris)
