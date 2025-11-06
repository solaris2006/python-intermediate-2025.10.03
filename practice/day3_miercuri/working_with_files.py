# working with files


f = open("file.txt")

# notă #1:
# default mode: text
# implicație: se face o conversie din bytes în ce vedem noi,
# conform encoding-ului

# notă #2:
# encoding-ul, dacă nu este specificat, va fi
# default-ul platformei (linux: utf-8, windows: cp1252)

# notă #3:
# dacă fac f.read() repetat,
# returnează string gol

# notă #4:
# f.tell() returnează poziția în bytes
# a cursorului

# notă #5:
# un file pointer este iterabil. [!!!]
# în modul text, line by line


# știind că docstring-ul este în atributul `__doc__`,
# știind că `open()` cu al 2lea parametru "w"
#   deschide un fișier în mod text write,
# știind că obiectul returnat are metoda `.write()`,
#
# creați un fișier "open_docs.txt" care să conțină
# docstringul funcției open.

f = open("open_docs.txt", "w")
content = open.__doc__
f.write(content)

# dacă nu găsiți nimic în fișier,
# rulați f.close()


# notă #6:
# write-ul se face buffer-uit.
# dacă vrem să ne asigurăm că a ajuns pe disc,
# facem .flush() explicit.


# notă #7:
# vrem să facem .close()
f.close()


def writestuff(fname1, fname2, fname3):
    try:
        fp1 = open(fname1, "w")
        fp2 = open(fname2, "w") # « a crăpat aici
        fp3 = open(fname3, "w")
    finally:
        fp1.close()
        fp2.close()
        fp3.close() # excepție


# notă 8: s-au schimbat mult lucrurile,
# cu introducerea context manager-ilor:

with open("open_docs.txt", "w") as fp:
    content = open.__doc__
    fp.write(content)

# Exercițiu:
# scrieți o funcție
def grep(fname: str, txt: str):
    pass
# ce face print tuturor liniilor din fișierul "fname"
# care conțin string-ul `txt`

"""
fname = "open_docs.txt"

with open(fname) as fp:
    counter = 0

    lines = fp.readlines() # <<-- tocmai am alocat niște memorie

    for line in lines:
        print(line, end="")
        if counter > 4: break
        counter += 1

with open(fname) as fp: # <<-- citește linia, nu alocă altă memorie
    counter = 0
    for line in fp:
        print(line)
        if counter > 4: break
        counter += 1
"""

def grep(fname, txt):
    with open(fname) as fp:
        for line in fp:
            if txt in line:
                print(line, end="")

                if not line.endswith("\n"):
                    # this is the last line,
                    # and the file doesn't end with "\n"
                    print()

grep("open_docs.txt", "read")

# Exercițiu:
# scrieți o funcție
def cp(srcfile, destfile):
    "copies the `srcfile` file to `destfile`"
    pass

# v.1. posibil bubuie memorie.
def cp(src, dst):
    with open(src) as s:
        with open(dst, "w") as d:
            d.write(
                s.read()
            )

# v.2. line by line. it much better is.
def cp(src, dst):
    with open(src) as s:
        with open(dst, "w") as d:
            for line in s:
                d.write(line)

# v.3. binary files we can do now.
def cp(src, dst, chunk=4096): #kwarg = keyword argument
    with open(src, "rb") as s, \
         open(dst, "wb") as d:
        # let's read and write in chunks
        while content := s.read(chunk):
            d.write(content)
