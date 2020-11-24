#!/usr/bin/env python3
import requests, sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("You forgot an argument")
    exit(0)
r = requests.get("https://mangadex.org/api/v2/manga/{}/covers".format(url))
manga = r.json()
for img in manga["data"]:
    for cover in img.values():
        print(cover)
