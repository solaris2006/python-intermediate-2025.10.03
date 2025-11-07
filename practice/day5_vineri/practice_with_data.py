# read the "books.csv" file
# and group all books
# by Genre

import csv
import json
from collections import defaultdict


f = open("data/books.csv")
reader = csv.DictReader(f)

genres = defaultdict(list)

for book in reader:
    genre = book.pop('Genre')

    # problemă: vrem să accesăm
    # o cheie care nu există încă.

    # rezolvări posibile:
    # a) verificăm manual dacă există
    #    if genre in genres: ...
    #    else: ...
    # b) try / except
    #    try:
    #        books = genres[genre]
    #    except KeyError:
    #        books = genres[genre] = []
    # c) folosesc o structură de date
    #    care se comportă ca un dicționar
    #    dar dacă nu există cheia o creează

    genres[genre].append(book)


# json: javascript object notation

# Exercițiu: scrieți o funcție
def extract_genres(books_file, json_out_file):
    pass

# folosiți json.dump(obj, fp, indent=2)

def extract_genres(books_file, json_out_file):
    with open(books_file, encoding="utf-8") as f_in, \
         open(json_out_file, "w", encoding="utf-8") as f_out:
        
        reader = csv.DictReader(f_in)
        genres = defaultdict(list)

        for book in reader:
            genre = book.pop('Genre')
            genres[genre].append(book)

        json.dump(genres, f_out, indent=2)

extract_genres("data/books.csv", "books_by_genre.json")

# json.dumps / json.loads # lucrează pe string-uri
# json.dump / json.load # lucrează pe file pointere


# lucrat cu requests
resp = requests.get("https://example.com")

resp.text # str, already decoded from resp.encoding
resp.body # the actual response body, in bytes. you won't need it.

# lucrat cu requests cu json
resp = requests.get("https://jsonplaceholder.typicode.com/todos")
data = resp.json()

# pretend that we are a browser:
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
resp = requests.get("https://ash-speed.hetzner.com/10GB.bin", headers=headers)

# go into streaming mode.
# we want to stream when A) downloading a huge file:
resp = requests.get("https://ash-speed.hetzner.com/10GB.bin", headers=headers, stream=True)

with open("out.file", "wb") as outf:
    for chunk in resp.iter_content():
        outf.write(chunk)
        #outf.flush() # we don't usually want to do this

# we also want to stream when B) we want to iterate over the response
# in a controlled manner:

# note: start a server using
# $ python http_serve_gzip.py
url = "http://localhost:8081/"

import requests
from datetime import time
from decimal import Decimal

def fetch_csv(url):
    response = requests.get(url, stream=True)

    data = csv.reader(
        response.iter_lines(decode_unicode=True)
    )

    for t, v in data:
        # pentru scientific data și pentru financial data
        # folosim un data-type care nu este float!
        #if t == "time":
        #    continue

        yield (
            time(*map(int, t.split(":"))),
            Decimal(v)
        )
