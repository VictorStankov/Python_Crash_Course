def make_album(artist, title, n_tracks=""):
    output = {"artist name": artist, "album title": title}
    if n_tracks:
        output['tracks'] = n_tracks
    return output


print(make_album('idk', 'any albums', str(3)))
print(make_album('how tf', 'should I know'))
print(make_album('the point is', "I'm doing it", str(50)))
