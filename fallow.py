#!/usr/bin/env python3
import sys, json

allowed_states = ["completed", "reading", "plan to read", "on hold", "dropped"]

def SearchStatus(status):
    for num,i in enumerate(chapters["fallows"]):
        if i["status"] in status:
            print("{}. {} - {}".format(num, i["title"], i["status"]))

def GetProgress(pos):
    # This could probably be done better.
    finished = []
    total = 0
    for p in chapters["fallows"][pos]["chapters"]:
        for c in p:
            if p[c] == "completed":
                finished.append(c)
                total += 1
            else:
                total += 1
    return str(len(finished)) + "/" + str(total)

def ChangeStatus(pos, status):
    chapters["fallows"][pos]["status"] = status
    with open('chapters.json', 'w') as f:
        json.dump(chapters, f, indent=2)

def Info(pos):
    print("Title: {}\nStatus: {}\nChapters Completed: {}".format(chapters["fallows"][pos]["title"], chapters["fallows"][pos]["status"], GetProgress(pos)))

if __name__ == "__main__":
    with open('chapters.json', 'r') as f:
        chapters = json.load(f)
    if len(sys.argv) > 2 and sys.argv[1] == "i":
        Info(int(sys.argv[2]))
    elif len(sys.argv) > 1 and sys.argv[1] == "l":
        SearchStatus(allowed_states)
    elif len(sys.argv) > 2 and sys.argv[1] == "fs":
        if sys.argv[2] in allowed_states:
            SearchStatus(sys.argv[2])
    elif len(sys.argv) > 3 and sys.argv[1] == "cs":
        if sys.argv[3] in allowed_states:
            ChangeStatus(int(sys.argv[2]), sys.argv[3])
