# iterații


iterable = "un string" # string-ul este iterabil char by char
iterable = ["un", "element", "și altul"]
iterable = range(10)

for element in iterable:
    print("elem: ", element)


# sequences:
# - they all have access by index (and also by slice)
# - they are all iterable
# - they all have a .count() method
# - they all have an .index() method

# str
"abcdefg"
# immutable

# tuple
("lalala", "lululu")
# immutable

# list
["lalala", "lululu"]
# mutable
# 


# Exercițiu:
# dat fiind range(10),
# creați o listă ce conține pătratele fiecărui număr

# strategie:
# 1. inițializăm o listă goală
lst = []

# 2. iterăm prin iterabilul sursă
for x in range(10):
    # 3. construim lista »» lst.append(valoare) 
    lst.append(x * x)

# 4. este gata
print(lst)


# Exercițiu:
# dat fiind range(10),
# creați o listă ce conține pătratele fiecărui număr impar

# strategie:
# 1. inițializăm obiectul
lst = []

# 2. iterăm prin sursă
for x in range(10):
    # 3. verificăm condiție
    if x % 2:
        # 4. construim obiectul
        lst.append(x * x)

# 5. gata
print(lst)

# Exercițiu
# o funcție care generează o parolă
# folosind toate caracterele dintre '!' și '~' (inclusiv).
#
# ce știm:
# - există funcțiile `ord()` și `chr()`
# - există `random.randint()` (care este inclusiv)

import random

start = ord('!')
end = ord('~')

def genpasswd(length):
    passwd = ''

    #for _ in range(length):
    while len(passwd) < length:
        passwd += chr(random.randint(start, end))
        
    return passwd

# v.2: ne pre-generăm lista de caractere,
#      și folosim `random.choice()`
PASSWD_CHARS = ""
for num in range(start, end + 1):
    PASSWD_CHARS += chr(num)


def genpasswd(length):
    # optimisation: using a list instead of
    # appending to string
    passwd = []

    while len(passwd) < length:
        passwd.append(random.choice(PASSWD_CHARS))

    return ''.join(passwd)

