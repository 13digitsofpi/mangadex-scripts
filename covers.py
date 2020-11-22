#!/usr/bin/env python3
import cloudscraper, sys, json

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = ""
    while url == "":
        url = input("Those numbers in the url: ").strip()
scraper = cloudscraper.create_scraper()
try:
    r = scraper.get("https://mangadex.org/api/v2/manga/{}/covers".format(url))
    manga = json.loads(r.text)
except (json.decoder.JSONDecodeError, ValueError) as err:
    print("CloudFlare error: {}".format(err))
    exit(1)
covers = []
for img in manga["data"]:
    for cover in img.values():
        print(cover)
    #covers.append(img)

