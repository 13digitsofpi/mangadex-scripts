#!/usr/bin/env python3
import requests, sys

# language, default english
lang_code = 'gb'
# tad-id returned by mangadex to tag name
genre = {
    1: "4-Koma",
    2: "Action",
    3: "Adventure",
    4: "Award Winning",
    5: "Comedy",
    6: "Cooking",
    7: "Doujinshi",
    8: "Drama",
    9: "Ecchi",
    10: "Fantasy",
    11: "Gyaru",
    12: "Harem",
    13: "Historical",
    14: "Horror",
    16: "Martial Arts",
    17: "Mecha",
    18: "Medical",
    19: "Music",
    20: "Mystery",
    21: "Oneshot",
    22: "Psychological",
    23: "Romance",
    24: "School Life",
    25: "Sci-Fi",
    28: "Shoujo Ai",
    30: "Shounen Ai",
    31: "Slice of Life",
    32: "Smut",
    33: "Sports",
    34: "Supernatural",
    35: "Tragedy",
    36: "Long Strip",
    37: "Yaoi",
    38: "Yuri",
    40: "Video Games",
    41: "Isekai",
    42: "Adaptation",
    43: "Anthology",
    44: "Web Comic",
    45: "Full Color",
    46: "User Created",
    47: "Official Colored",
    48: "Fan Colored",
    49: "Gore",
    50: "Sexual Violence",
    51: "Crime",
    52: "Magical Girls",
    53: "Philosophical",
    54: "Superhero",
    55: "Thriller",
    56: "Wuxia",
    57: "Aliens",
    58: "Animals",
    59: "Crossdressing",
    60: "Demons",
    61: "Delinquents",
    62: "Genderswap",
    63: "Ghosts",
    64: "Monster Girls",
    65: "Loli",
    66: "Magic",
    67: "Military",
    68: "Monsters",
    69: "Ninja",
    70: "Office Workers",
    71: "Police",
    72: "Post-Apocalyptic",
    73: "Reincarnation",
    74: "Reverse Harem",
    75: "Samurai",
    76: "Shota",
    77: "Survival",
    78: "Time Travel",
    79: "Vampires",
    80: "Traditional Games",
    81: "Virtual Reality",
    82: "Zombies",
    83: "Incest",
    84: "Mafia",
    85: "Villainess"
}

def GetGenInfo(mid):
    r = requests.get("https://mangadex.org/api/v2/manga/{}/".format(mid))
    manga = r.json()
    title = manga["data"]["title"]
    artist = manga["data"]["artist"]
    author = manga["data"]["author"]
    ratings = manga["data"]["rating"]["mean"]
    print("{}\nBy {} and {}\nRated: {}".format(title, author, artist, ratings))
    for tag in manga["data"]["tags"]:
        print(genre[tag])

def ListChapters(mid):
    r = requests.get("https://mangadex.org/api/v2/manga/{}/chapters".format(mid))
    chapters = r.json()
    for chap in chapters["data"]["chapters"]:
        if chap["language"] == lang_code:
            print(chap["chapter"], chap["title"])

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[2]
        if sys.argv[1] == "i":
            GetGenInfo(url)
        elif sys.argv[1] == "c":
            ListChapters(url)
