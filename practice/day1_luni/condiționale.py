# condiționale

"""
# form 1
if expresie:
    logica


# form 2
if expresie:
    logica
else:
    logica_alt


# form 3
if expresie_1:
    logica_1

elif expresie_2:
    logica_2

# ...

elif expresie_n:
    logica_n


# form full
if expresie_1:
    logica_1

elif expresie_2:
    logica_2

# ...

elif expresie_n:
    logica_n
 
else:
    logica_x
"""


# Exercițiu
# luați cu input() vârsta utilizatorului
# și dacă este mai în vârsta de 18 ani,
# faceți print cu "vârstă validă", altfel cu
# "vârstă invalidă"

age = input("Vârsta ta? ")
age = int(age)

if age >= 18:
    print("Ok")
else:
    print("Too young")


# modificare cerință:
# sub 18 ani: "prea tânăr"
# peste 85 ani: "prea bătrân"
# între 18 și 85 inclusiv: "acceptat"

age = int(input("Vârsta ta? "))

if age < 18: # [-inf, 18)
    print("Prea tanar")
elif age > 85: # (85, inf]
    print("Prea batran")
else:
    print("OK")


if age >= 18 and age <= 85:
    print("OK")
elif age > 85: # (85, inf]
    print("Prea batran")
else:
    print("Prea tânăr")


if 18 <= age <= 85:
    print("OK")
elif age > 85: # (85, inf]
    print("Prea batran")
else:
    print("Prea tânăr")


"""
while condiție:
    do_something()
    do_something_else()
"""

# Exercițiu:
# cerem utilizatorului o parolă.
# este obligatoriu ca parola să aibă minim 5 caractere

#password = input("Input password ")

# Pattern 1: iterație infinită,
#            ieșim din ea cu break

while True:
    password = input("Input password ")
    if len(password) >= 5:
        print("Succes")
        break
    else:
        print("Error. Need longer pass")


# Pattern 2: iterație infinită,
#            repetăm dacă nu ne convine
#            ieșim din ea cu break la final (dacă ne convine)

while True:
    password = input("Input password ")
    if len(password) < 5:
        print("Error. Need longer pass")
        continue

    print("Succes")
    break


# Pattern 3: base pattern.
#            condiția while-ului este cea care ne interesează

password = input("Input password ")

while len(password) < 5:
    print("Error. Need longer pass")
    password = input("Input password ")


# Pattern 4: using the "walrus" operator

while password := input("Input password "):
    if len(password) >= 5:
        print("Succes")
        break

    # else:
    print("Error. Need longer pass")




