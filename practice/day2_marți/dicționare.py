# dicționare

# structură de date de tip
# cheie: valoare

# k1: v1,
# k2: v2,
# ...

{
  'Name': 'Gigel',
  'Age': '20',
  'City': 'Copenhaga'
}

dict(Name='Gigel', Age='20', City='Copenhaga')


# Exercițiu:
# dat fiind raportul primit ca string cu acest format
s = """-----------------------------------
|####Name####|#Age#|#####City#####|
-----------------------------------
| Gigel      |  20 | Copenhaga    |
| Andrei     |  42 | București    |
| Georgiana  |  20 | Timișoara    |
| Andreea    |  20 | Constanța    |
| Carmencita |  20 | Satu Mare    |
| George     |  20 | Sfântu Gheor |
-----------------------------------"""

# scrieți o funcție `parse_report(txt)`
# ce returnează o listă de dicționare
# de forma
# [
#     {'Name': 'Gigel', 'Age': '20', 'City': 'Copenhaga'},
#     {'Name': 'Andrei', 'Age': '42', 'City': 'București'},
#     ...
# ]


def parse_report(s):
    out = []

    lines = s.split("\n")
    header = parse_header(lines[1])

    for r in lines[3:-1]:
        row = parse_row(r)
        out.append(
            dict(zip(header, row))
        )

    return out

print(parse_report(s))

# the brute force version
# (nu știm că se poate dict(zip()))

def parse_report(txt):
    list = []
    lines = txt.split("\n")
    header = parse_header(lines[1])    
    for r in lines[3:-1]:
        row = parse_row(r)

        d = {}
        for idx in range(len(header)):
            d[header[idx]] = row[idx]

        list.append(d)
    return list

# updated brute force version,
# with enumerate

def parse_report(txt):
    list = []
    lines = txt.split("\n")
    header = parse_header(lines[1])    
    for r in lines[3:-1]:
        row = parse_row(r)

        d = {}
        for idx, col in enumerate(header):
            d[col] = row[idx]

        list.append(d)
    return list


# modalitățile de a face ceva când o cheie nu există:
d = {'Name': 'Andreea', 'Age': '20', 'City': 'Constanța'}

# 1. acces direct
try:
    v = d["woot"]
except KeyError:
    print("nu avem cheie") # extra-logică
    v = "---"

#2. testăm explicit
if "woot" in d:
    v = d["woot"]
else:
    print("nu avem cheie") # extra-logică
    v = "---"

#3. folosind .get()
v = d.get("woot", "---") # facem direct retrieval


# Exercițiu
# dat fiind un string
s = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."

# creați un dicționar cu cheia fiecare cuvânt din `s`,
# și valoarea numărul de apariții al cuvântului în `s`

# (reformulat: scrieți o funcție `count_words(s)` ce numără
# de câte ori apare fiecare cuvânt în s)


# să înlocuim toate caracterele "non-word" cu spațiu.
# o să folosim translation table

import string

SPLITCHARS = "".join([
    c for c in string.punctuation
    if c not in ('-', '_')
])

PUNCTUATION_TABLE = str.maketrans(SPLITCHARS, " " * len(SPLITCHARS))

def count_words(s):
    # s = s.lower()
    
    s = s.translate(PUNCTUATION_TABLE)
    words = s.split()
    
    counts = {}
    for word in words:
        # v.1, cu if
        # if word in counts:
        #     counts[word] += 1
        # else:
        #     counts[word] = 1

        # v.2, cu get
        old_value = counts.get(word, 0)
        counts[word] = old_value + 1
    
    return counts


# v.3, cu defaultdict
# also, `insensitive` e argument opțional

from collections import defaultdict

def count_words(s, insensitive=False):
    if insensitive:
        s = s.casefold()
    
    s = s.translate(PUNCTUATION_TABLE)
    words = s.split()
    
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    
    return counts



distances = {
    'București': 0,
    'Iași': 20,
    'Cluj': 30,
}

while distances:
    city, distance = distances.popitem()
    print("processing", city, "(%s)" % distance)
