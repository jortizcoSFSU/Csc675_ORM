# This file is to perform tests to models such as getting a record, inserting, updating ...

from models.models import Artist, Album

# create a new album in the database
album = Album.create(title="new album", year_release=2000)

# get an existing album from the database with id=1
album1 = Album.get(id=1)

# update the title of an existing album in the database
album1.title = "New title"
album.save()

# get all albums from the database
albums = Album.all()












