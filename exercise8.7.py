def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "album": album_title
    }

    if number_of_songs is not None:
        album["number_of_songs"] = number_of_songs

    return album

album1 = make_album("Nadin Amizah", "Selamat Ulang Tahun")
album2 = make_album("Tulus", "Manusia")
album3 = make_album("Hindia", "Menari dengan Bayangan")

print(album1)
print(album2)
print(album3)

album4 = make_album("Cortis", "GreenGreen", 8)

print(album4)
