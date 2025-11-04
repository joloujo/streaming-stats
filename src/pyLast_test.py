from dotenv import load_dotenv
import os
import pylast
import json

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('PYLAST_API_KEY')
API_SECRET = os.getenv('PYLAST_API_SECRET')

if API_KEY == None or API_SECRET == None:
    if API_KEY == None:
        print('API Key not found')
    if API_SECRET == None:
        print('API Secret not found')
    print('Exiting')
    exit()

network = pylast.LastFMNetwork(API_KEY, API_SECRET)
network.enable_rate_limit()
print(network.is_rate_limited())

# track: pylast.Track = network.get_track_by_mbid('aaf2a923-a62d-4cf8-abc8-9809c76dd7a8')
# track: pylast.Track = network.get_track_by_mbid('3d35426f-911f-4413-b11c-89003b88ab83')
# track: pylast.Track = network.get_track('Regina Spektor', 'Better')
# track: pylast.Track = network.get_track('Big Thief', 'Change')

# print(track.get_artist())
# print(track.get_name())
# print(track.get_album())
# print(track.get_duration())

# user = network.get_user('joloujo')
# tracks = user.get_recent_tracks(limit=1)

# print(tracks)