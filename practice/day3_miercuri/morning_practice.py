# Exercițiu:
# Create a dictionary called person that contains the following key-value pairs:
#  "name": "Jane"
#  "age": 32
#  "occupation": "teacher"
#  "hobbies": ["reading", "hiking"]

person = {
    "name": "Jane",
    "age": 32,
    "occupation": "teacher",
    "hobbies": ["reading", "hiking"],
}

#     print the value for key age
print(person["age"])

#     update the value for key age to 52
person["age"] = 52

#     add a new item to the dictionary with key "friends" and value ["Anna", "Grace", "Mike"]
person["friends"] = ["Anna", "Grace", "Mike"]

#     add "cooking" to the hobbies list
person["hobbies"].append("cooking")

#     print the dictionary and its length
print(person)
print(len(person))


# Exercițiu:
# Using the person dictionary above:
# - Remove key occupation and save its value in a variable; print the variable.
occupation = person.pop("occupation")
print(occupation)

# - Try getting the value for key height (or None, if key does not exist) from the dictionary and store it in a variable; print the variable.
height = person.get("height", 0)
print(height)

# - Update the dictionary with the following dictionary:
#   measurements = {"weight": 75, "height": 1.78, "name": "John"}
measurements = {"weight": 75, "height": 1.78, "name": "John"}
person.update(measurements)

# - Iterate on the dictionary to print its keys and values.
for k, v in person.items():
    print(f'key is: {k} value is: {v}')


#Exercițiu:
# Dată fiind o structură de date de forma:
people = [
    ("Jane", 20, ["reading", "hiking", "biking"]),
    ("Mike", 17, ["hiking", "fishing"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
]
# creați o structură de date nouă
# ce conține o listă de dicționare de forma
# [
#     {
#         'name': 'Jane',
#         'age': 52,
#         'hobbies': ['reading', 'hiking', 'biking'],
#     },
#     ...
# ]
persons = []
for name, age, hobbies in people:
    persons.append({
        "name": name,
        "age" : age,
        "hobbies" : hobbies
    })

# v2: folosind zip
keys = ("name", "age", "hobbies")
persons = []
for person in people:
    persons.append(
        dict(zip(keys, person))
    )


# Exercițiu:
# dată fiind lista de dicționare obținută mai sus,
# și dat fiind dicționarul cu informații adiționale
# despre fiecare persoană:
occupations = {
    'Sam': 'firefighter',
    'Dan': 'cook',
    'Anna': 'writer',
    'Jane': 'teacher',
}
# găsiți o modalitate să updatați dicționarul potrivit
# din listă, adăugându-i cheia "occupation".

# A. iterăm prin toate persoanele
for person in persons: # person is a dict
    name = person['name']
    try:
        occ = occupations[name]
    except KeyError:
        # there was no update
        continue

    person["occupation"] = occ


# B. cum facem dacă suntem obligați să iterăm
#    prin dicționarul nou?

for name, occ in occupations.items():
    for person in persons:
        if person['name'] == name:
            # we have a match!
            person["occupation"] = occ
            break


# Construiți-vă un dicționar "cities" de forma
# {
#     'Jane': "București",
#     'Mike': "Cluj",
#     ...
# }
# folosind numele din persons, și orașele
c = ["București", "Cluj", "Timișoara", "Iași", "Constanța"]

cities = dict(zip([p['name'] for p in persons], c))


# Exercițiu
# având lista de dicționare
persons = [
    {'id': 215, 'name': 'Jane', 'age': 20, 'hobbies': ['reading', 'hiking', 'biking']},
    {'id': 220, 'name': 'Yvonne', 'age': 32, 'hobbies': []},
    {'id': 282, 'name': 'Mike', 'age': 17, 'hobbies': ['hiking', 'fishing']},
    {'id': 283, 'name': 'Anna', 'age': 25, 'hobbies': []},
    {'id': 292, 'name': 'Sam', 'age': 40, 'hobbies': ['playing guitar']},
    {'id': 302, 'name': 'Dan', 'age': 34, 'hobbies': ['painting', 'reading']}
]
# presupunând că persons are 10 milioane de elemente,
# și primind update-uri de forma:
updates = {
    "occupation": {
        215: "firefighter",
        220: "cook",
        292: "writer",
        283: "teacher"
    },
    "city": {
        215: "București",
        302: "Cluj",
        292: "Timișoara",
        283: "Iași",
        220: "Constanța"
    }
}
# Întrebare:
# cum faceți update eficient elementelor din listă
# (fiecărui dicționar de persoană în parte) ??

# Răspuns:
# folosim o structură de date ce ne permite lookup eficient
# între cheia folosită (`name`) și »» obiectul corespunzător ««
# (adică dicționarul din lista persons)

# declarăm obiectul
persons_dict = {}
# iterăm în sursă
for person in persons:
    id = person['id']
    # construim
    persons_dict[id] = person

# {k: v for k, v in source}

# cu dict comprehension:
persons_dict = {
    person['id'] : person
    for person in persons
}


for key, batch in updates.items():
    for id, value in batch.items():
        persons_dict[id][key] = value



# Exercițiu:
# găsește toți prietenii care au hiking printre hobby-uri
#
# folosește funcția `filter()`

filter(
    lambda elem: 'hiking' in elem['hobbies'],
    persons_dict.values() # the same with persons
)
