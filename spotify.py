import spotipy

sp = spotipy.Spotify()

results = sp.search(q="weezer", limit=20)

for i, t in enumerate(results["tracks"]["items"]):
    print(" ", i, t["name"])


def signin(email, password):
    # TODO: Add spotify signin logic here
    pass
