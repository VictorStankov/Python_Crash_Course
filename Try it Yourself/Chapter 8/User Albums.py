def make_album(artist, title, n_tracks=""):
    output = {"artist name": artist, "album title": title}
    if n_tracks:
        output['tracks'] = n_tracks
    return output


while True:
    print("\nPlease enter an artist's name, title of their album and the number of tracks"
          " if you so happen to know that:")
    print("(you can write 'q' to quit at any time)")
    ar_name = input("Artist name: ")

    if ar_name == 'q':
        break

    al_title = input("Album title: ")
    if al_title == 'q':
        break

    tracks = input("Number of tracks (Optional): ")
    if tracks == 'q':
        break

    print(make_album(ar_name, al_title, tracks))
