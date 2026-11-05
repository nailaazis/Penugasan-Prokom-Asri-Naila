def make_album(artist_name, album_title):
    album = {
        "artist": artist_name,
        "album": album_title
    }

    return album

while True:
    print("\nMasukkan informasi album:")
    print("(Ketik 'quit' untuk berhenti)")

    artist = input("Nama artis: ")

    if artist.lower() == "quit":
        break

    title = input("Judul album: ")

    if title.lower() == "quit":
        break

    album_info = make_album(artist, title)
    print("Informasi album:")
    print(album_info)

print("\nProgram selesai. Terima kasih!")
