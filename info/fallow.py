#!/usr/bin/env python3
import sys, json

# status allowed as parameter 
allowed_states = ["completed", "reading", "plan to read", "on hold", "dropped"]

# searches in chapters.json titles that have the status equal to status
def SearchStatus(status):
    for num,i in enumerate(chapters["fallows"]):
        if i["status"] in status:
            print("{}. {} - {}".format(num, i["title"], i["status"]))

# counts total chapters and chapters marked as completed
def GetProgress(pos):
    finished = 0
    total = 0
    for p in chapters["fallows"][pos]["chapters"]:
        for c in p:
            if p[c] == "completed":
                finished += 1
            total += 1
    return str(finished) + "/" + str(total)

# change key value of status to status
def ChangeStatus(pos, status):
    chapters["fallows"][pos]["status"] = status
    with open('chapters.json', 'w') as f:
        json.dump(chapters, f, indent=2)

# prints information from the previous functions and chapters.json
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
