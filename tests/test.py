# This file is to perform tests to models such as getting a record, inserting, updating ...

# We covered last lecture:

from models.models import Album, Track

track7 = Track.get(id=7) # track_id = 7
track9 = Track.get(id=9) # track_id = 9

album1 = track7.album_object # album_id = 5
album2 = track9.album_object # album_id = 5

track7_ref = album1.track
track9_ref = album2.track

print(track7_ref is track7)


# Imagine an album has many tracks

track7 = Track.get(id=7) # track_id = 7
album1 = track7.album_object # album_id = 5
all_tracks = album1.tracks






