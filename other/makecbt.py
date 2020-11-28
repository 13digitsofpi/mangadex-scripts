#!/usr/bin/env python
import tarfile, sys

# Makes a .cbt file from a chapter
def makecbt(mangapath, name):
    arc = tarfile.open(name + '.cbt', 'w|gz')
    arc.add(mangapath)
    arc.close()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        makecbt(sys.argv[1], sys.argv[2])
