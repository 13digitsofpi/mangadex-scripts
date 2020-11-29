#!/usr/bin/env python3
import requests, sys, os

# This script was based of frozenpandaman/mangadex-dl

# Language to download, default english
lang_code = "gb"

def dl(c2d, url, downloads_dir):
    # scrape the api
    r = requests.get("https://mangadex.org/api/v2/manga/{}/chapters".format(url))
    manga = r.json()
    #list all the chapters that have language equal to lang_code 
    chapters = []
    for chap in manga["data"]["chapters"]:
        if chap["language"] == lang_code:
            for vc in c2d.split(","):
                if chap["chapter"] == vc:
                    chapters.append(chap["id"])

    if len(chapters) == 0: 
        print("No Chapters (see if you put it in right)")
        exit(0)
    # get the url for the downloading the pages
    for p in chapters:
        r = requests.get("https://mangadex.org/api/v2/chapter/{}".format(p))
        page = r.json()
        images = []
        server = page["data"]["server"]
        hashcode = page["data"]["hash"]
        for pg in page["data"]["pages"]:
            images.append("{}{}/{}".format(server, hashcode, pg))

        print("Downloading Chapter {}".format(page["data"]["chapter"]))
        for num,l in enumerate(images, 1):
            output_dir = os.path.join(downloads_dir, str(page["data"]["mangaId"]), page["data"]["chapter"])
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            if num < 10:
                outfile = os.path.join(output_dir, "00" + str(num) + os.path.splitext(l)[1])
            elif num > 10 and num < 100:
                outfile = os.path.join(output_dir, "0" + str(num) + os.path.splitext(l)[1])
            r = requests.get(l)
            if r.status_code == 200:
                with open(outfile, 'wb') as f:
                    f.write(r.content)
            else:
                print("Encountered Error while Downloading")

            print(" Downloaded page {}.".format(num))
        print("Downloaded Chapter {}".format(page["data"]["chapter"]))

if __name__ == "__main__":
    if len(sys.argv) > 3:
        mid = sys.argv[1]
        dlchaps = sys.argv[2]
        ddir = sys.argv[3]
    else:
        print("{} manga-id, chapters, download directory".format(sys.argv[0]))
        exit(0)

    dl(dlchaps, mid, ddir)
