## Scripts

* Covers -- Lists Covers for Manga
* Dl -- Downloads Chapter(s)
* Info -- Info about Manga
* Fallow -- Manage fallows in json.


### Covers

Requires a manga id _e.g_ 15160 as an argument or input. 

**Example usage:**

`./covers.py 11560`

Would output something similar to:

```
1.1
https://mangadex.org/images/covers/15160v1.1.jpg?1569693672
1.2
https://mangadex.org/images/covers/15160v1.2.jpg?1569693697
2.1
https://mangadex.org/images/covers/15160v2.1.jpg?1569693727
2.2
https://mangadex.org/images/covers/15160v2.2.jpg?1569693756
````

### Dl

Requires a manga id _e.g_ 15160, any number of chapters to download separated by commas, and the directory to write to, as an argument or input.

**Example usage:**

`./dl.py 15160 1,2,3 download`

Would output something similar to:

```
Downloads Chapter 1
    Page 1
    etc
```

The preferred language is stored in the variable lang_code, this might be subject to change if I add a config file.

#### Errors
If there are not any any chapters available, it will print an error and exit. 
If there was an error in downloading it will print an error but continue.

### Info

Requires a manga id _e.g_ 15160 as an argument or input.
Has a dictionary used for converting tag-ids to tag names.

Prints title, artist and author, and tags.

**Example usage** 

`./info.py 15160`

Would ouput something similar to:

```
T-REX na Kanojo
By ['Sanzo'] and ['Sanzo']
Rated: 8.14
Comedy
Fantasy
Romance
Slice of Life
Monster Girls
```

### Makecbt

Creates a .cbt file from a path. Takes the path and then the preferred name. You can omit .cbt from the name because it is added anyways.

**Example Usage**

`/.makecbt.py path/to/thing thing`

Doesn't output anything.

**Optional Dependencies:** A cb viewer, a good one is zathura.

Probably could of been done easier in sh or not at all.

### Fallows

Edits and reads `chapters.json`. 

**Arguments:**

* i _pos_ - Info - Prints associated info: title, status, and progress. 
* l - List - Lists all titles and their status.
* fs _pos_ - Filter Status - Lists but filtered based on status.
* cs _pos_ - Change Status - Changes status 
  
_pos_ is the index of the entry.
