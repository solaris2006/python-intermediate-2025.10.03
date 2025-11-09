# iterators

def repeat(v, num):
    for _ in range(num):
        yield v

for elem in repeat("bla", 7):
    print(elem)


# Exercițiu:
# scrieți o funcție generator
# def randgen(min, max, times=None):
#     pass
# aceasta returnează un generator
# care, când este consumat, yield-uiește un număr random între min și max.
#
# dacă `times` este dat, se oprește după `times` iterații.
# dacă `times` este `None`, continuă la nesfârșit.

import random


def randgen(min, max, times=None):
    while times is None:
        yield random.randint(min, max)

    for _ in range(times):
        yield random.randbytes(min, max)

def randgen(min, max, times=None):
    if times is None:
        while True:
            yield random.randint(min, max)
    else:
        for _ in range(times):
            yield random.randbytes(min, max)


# Exercițiu: transforming `grep`

# V.1: build output by manually appending

def grep(fname, txt):
    """
    returns all lines in `fname` that match `txt`
    as an iterable
    """

    out = []
    with open(fname) as fp:
        for line in fp:
            if txt in line:
                out.append(line.removesuffix("\n"))
    return out

# V.2: list comprehension

def grep(fname, txt):
    """
    returns all lines in `fname` that match `txt`
    as an iterable
    """

    with open(fname) as fp:
        return [
            line.removesuffix("\n")
            for line in fp
            if txt in line
        ]

# V.3: generator expression

def grep(fname, txt):
    """
    returns all lines in `fname` that match `txt`
    as an iterable
    """
    fp = open(fname)
    # face return unui generator
    return (
        line.removesuffix("\n")
        for line in fp
        if txt in line
    )

# 1. regulă:
# folosim întoteauna context manager pt. a lucra cu fișiere:
# with open(fname) as f:
#     do_something_with(f)

# 2. știm când să încălcăm regula:
# f = open(fname) 
# ....
    # 1) când este garantat că ieșim imediat din funcție
        # def func():
        #     f = open()
        #     return 

    # 2) când intenția mea este să păstrez filepointer-ul deschis!
    #    (ca de exemplu, am un iterator ce îl folosește în spate)

    # 3) când chiar vreau să fac close explicit când vreau eu,
    #    și am grijă să fac try / except în jurul codului
    #    dintre open() și .close()


# Exercițiu: (după masă)
# rescrieți funcția grep de mai sus
# drept o funcție generator.
# (adică face yield fiecărei linii corespunzătoare)



# facem grep o clasă iterabilă
# 1) implementează __iter__
# 2) implementează __next__
# 3) raise StopIteration

class grep:
    def __init__(self, fname, txt):
        self.file = open(fname)
        self.txt = txt

    def __iter__(self):
        return self
    
    def __next__(self):
        for line in self.file:
            if self.txt in line:
                return line.removesuffix("\n")
            
        # ^^ 1) este neterminat
        # și 2) nu am stabilit dacă merge, și dacă da, de ce


