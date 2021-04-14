import os
import spotipy
import json

from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Setup .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

# Store secret variables in .env file
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# print(SPOTIPY_CLIENT_ID)
# print(SPOTIPY_CLIENT_SECRET)
# print("something")

Kat_id = "3FX6ZjUpCoJOwsxleWx2ci"
kat = "spotify:artist:{}".format(Kat_id)

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

artist = sp.artist(kat)
albums = sp.artist_albums(kat)

data = {
    'external_urls': artist['external_urls']['spotify'],
    'followers_total': artist['followers']['total'],
    'spotify_id': artist['id'],
    'image': artist['images'][0]['url'],
    'name': artist['name'],
    'popularity': artist['popularity'],
    'type': artist['type'],
    'uri': artist['uri'],
}

# print(artist.get("followers").get("total"))
print(artist['popularity'])


def home(request):
    context = {
        "artist": artist,
        "albums": albums
    }

    return render(request, "spotify/home.html", context)

# Turns a dictionary into a class
# class Dict2Class(object):
#
#     def __init__(self, my_dict):
#         for key in my_dict:
#             setattr(self, key, my_dict[key])
#
#
# artist_object = Dict2Class(artist)


from api.views import ArtistSerializer

def add_data(request):
    # data = artist

    # json = data['student']
    # print("json:{}".format(json))
    serializer = ArtistSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        print("serializer was valid")
        thing = serializer.save()
        print("i made it to save")
        return render(request, "spotify/home.html", {"model": thing})
    else:
        print("serializer was not valid")
        print(serializer.errors)
        return
