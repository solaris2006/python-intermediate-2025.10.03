# sequences (str, list, tuple):
# - they all have access by index (and also by slice)
# - they are all iterable
# - they all support the `in` operator
# - they are all countable with `len()`
# - they all have a .count() method
# - they all have an .index() method



l = ['București', 'Cluj', 'Timișoara', 'Iași', 'Constanța', 'Satu Mare', 'Sfântu Gheorghe', 'Arad', 0, 1, 2, 3, 4, 'a', 'a', 'a', 'a', 'b']
# hai să ștergem tot ce vine după 0, inclusiv

# v1.
del l[l.index(0):] # wow

#v2. erasing the same indexing repeteadly
idx = l.index(0)

for _ in range(len(l) - idx):
    del l[idx]

#v3. erasing from the end
idx = l.index(0)
for i in range(len(l) - 1, idx - 1, -1):
    del l[i]

"""
There are 2 hard problems in computing:

- naming things
- cache invalidation
- off-by-one errors

"""

"""
There are 10 kinds of people in the world: those that understand binary and those that don't.
"""


# Exercițiu:
# sortați următoarea listă case-insensitive
l = ["ac", "aD", "ab", "Aa"]

def noop(v):
    return v.lower()

l.sort(key=noop)


# Exercițiu:
# dată fiind lista de tuple

l = [
    ('Jane', 25),
    ('Andrew', 33),
    ('John', 12),
    ('Michaela', 28)
]

# unde primul element este numele și al 2lea vârsta,
# sortați lista, in-place, după vârstă.

def sorter(v):
    return v[1]

l.sort(key=sorter)

# și cu lambda:

l.sort(key=lambda x: x[1])



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

# scrieți 2 funcții, `parse_header(txt)` și `parse_row(txt)`.
# ambele returnează o tuplă.
# rulați-le pe input-ul `s`, `parse_header` pe header,
# și `parse_row` pentru fiecare row în parte.

def parse_header(s):
    cols = []
    for col in s.split('|')[1:-1]:
        cols.append(col.strip('#'))
    return tuple(cols)

def parse_row(s):
    cols = []
    for col in s.split('|')[1:-1]:
        cols.append(col.strip(' '))
    return tuple(cols)

lines = s.split("\n")
header = parse_header(lines[1])
rows = []
for row in lines[3:-1]:
    rows.append(parse_row(row))



for name, age, city in rows:
    print(name, age)


# pentru fiecare row de mai sus, creați o listă de tuple
# de forma [(column1, value1), (column1, value1)]




# list comprehension
# să construim o listă de pătrate de range(5)

l = []
for x in range(5):
    l.append(x ** 2)

[x ** 2 for x in range(5)]


# să construim o listă de pătrate de range(9)
# dacă nr.-ul este impar

l = []
for x in range(9):
    if l % 2:
        l.append(x ** 2)

[
    x ** 2
    for x in range(9)
    if l % 2
]


