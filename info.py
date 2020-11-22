#!/usr/bin/env python3
import cloudscraper, sys, json

genre = {
    "1": "4-Koma",
    "2": "Action",
    "3": "Adventure",
    "4": "Award Winning",
    "5": "Comedy",
    "6": "Cooking",
    "7": "Doujinshi",
    "8": "Drama",
    "9": "Ecchi",
    "10": "Fantasy",
    "11": "Gyaru",
    "12": "Harem",
    "13": "Historical",
    "14": "Horror",
    "16": "Martial Arts",
    "17": "Mecha",
    "18": "Medical",
    "19": "Music",
    "20": "Mystery",
    "21": "Oneshot",
    "22": "Psychological",
    "23": "Romance",
    "24": "School Life",
    "25": "Sci-Fi",
    "28": "Shoujo Ai",
    "30": "Shounen Ai",
    "31": "Slice of Life",
    "32": "Smut",
    "33": "Sports",
    "34": "Supernatural",
    "35": "Tragedy",
    "36": "Long Strip",
    "37": "Yaoi",
    "38": "Yuri",
    "40": "Video Games",
    "41": "Isekai",
    "42": "Adaptation",
    "43": "Anthology",
    "44": "Web Comic",
    "45": "Full Color",
    "46": "User Created",
    "47": "Official Colored",
    "48": "Fan Colored",
    "49": "Gore",
    "50": "Sexual Violence",
    "51": "Crime",
    "52": "Magical Girls",
    "53": "Philosophical",
    "54": "Superhero",
    "55": "Thriller",
    "56": "Wuxia",
    "57": "Aliens",
    "58": "Animals",
    "59": "Crossdressing",
    "60": "Demons",
    "61": "Delinquents",
    "62": "Genderswap",
    "63": "Ghosts",
    "64": "Monster Girls",
    "65": "Loli",
    "66": "Magic",
    "67": "Military",
    "68": "Monsters",
    "69": "Ninja",
    "70": "Office Workers",
    "71": "Police",
    "72": "Post-Apocalyptic",
    "73": "Reincarnation",
    "74": "Reverse Harem",
    "75": "Samurai",
    "76": "Shota",
    "77": "Survival",
    "78": "Time Travel",
    "79": "Vampires",
    "80": "Traditional Games",
    "81": "Virtual Reality",
    "82": "Zombies",
    "83": "Incest",
    "84": "Mafia",
    "85": "Villainess"
}

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = ""
    while url == "":
        url = input("Those numbers in the url: ").strip()
scraper = cloudscraper.create_scraper()
try:
    r = scraper.get("https://mangadex.org/api/v2/manga/{}/".format(url))
    manga = json.loads(r.text)
except (json.decoder.JSONDecodeError, ValueError) as err:
    print("CloudFlare error: {}".format(err))
    exit(1)

title = manga["data"]["title"]
artist = manga["data"]["artist"]
author = manga["data"]["author"]
ratings = manga["data"]["rating"]["mean"]

print("{}\nBy {} and {}\nRated: {}".format(title, author, artist, ratings))

for tag in manga["data"]["tags"]:
    print(genre[str(tag)])
