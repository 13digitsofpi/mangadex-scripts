#!/usr/bin/env python3
import cloudscraper, sys, json, os

# Language to download
lang_code = "gb"

def dl(c2d, url, downloads_dir):
    scraper = cloudscraper.create_scraper()
    try:
        r = scraper.get("https://mangadex.org/api/v2/manga/{}/chapters".format(url))
        manga = json.loads(r.text)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        exit(1)
    chapters = []
    for chap in manga["data"]["chapters"]:
        if chap["language"] == lang_code:
            for vc in c2d.split(","):
                if chap["chapter"] == vc:
                    chapters.append(chap["id"])

    if len(chapters) == 0: 
        print("No Chapters (see if you put it in right)")
        exit(0)

    for p in chapters:
        try:
            r = scraper.get("https://mangadex.org/api/v2/chapter/{}".format(p))
            page = json.loads(r.text)
        except (json.decoder.JSONDecodeError, ValueError) as err:
            print("CloudFlare error: {}".format(err))
            exit(1)
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
            outfile = os.path.join(output_dir, str(num))
            r = scraper.get(l)
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
