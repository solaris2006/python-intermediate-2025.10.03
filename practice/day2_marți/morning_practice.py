#1. creați un string cu stringul "tra la la" repetat de 3 ori.
"tra la la" * 3

#2. obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4

#3. obțineți restul împărțirii lui 17 la 4.
17 % 4

#4. date fiind variabilele
name = "Jane"
is_student = True

# scrieți un if / else care să printeze
# "Jane is a student" / "Jane is not a student"
# concatenând variabila `name` cu restul stringului.

# executați, apoi înlocuiți
name = "Andrew"
is_student = False
# și executați din nou.


if is_student:
    print(name + " is a student")
else:
    print(name + " is not a student")



#5. dat fiind string-ul
s = "Bună dimineață"

# obțineți al 7lea caracter din string
s[6]


# obțineți penultimul caracter din string
s[-2]

# obțineți slice-ul până la al 4lea caracter
s[:4]

# slice-ul cu ultimele 7 caractere
s[-7:]

# știind că sintaxa completă de slice este [start:stop:step],
# obțineți fiecare al 2lea caracter
s[1::2]

# știind că sintaxa completă de slice este [start:stop:step],
# obțineți string-ul citit de la dreapta la stânga
s[::-1]

# verificați dacă începe cu "Bu"
s.startswith("Bu")

# verificați dacă se termină cu "aa"
s.startswith("aa")

# printați-i lungimea
len(s)

# numărați apariția caracterului "a" în `s`
s.count("a")


#6. scrieți o funcție `cube(x)` ce calculează x
# la puterea a 3a.

def cube(x):
    return x ** 3

#7. luați un număr întreg ca input de la utilizator.
# dacă input-ul nu este număr întreg valid, repetați input().
# folosiți funcția `cube()` pentru a calcula rezultatul
# și faceți print, folosind metoda `.format()`, cu textul:
# "Cubul numărului {number} este {cube}."


"""
# string formatting:
"%s %d %f" % (1, 2, 3)

"{} {}".format(1, 2, 3)
"{a} {b} {c}".format(a=1, b=2, c=3)
"""

while True:
    v = input("INTRODUCETI UN NUMAR: ")
    if v.isdecimal():
        break

v = int(v) # <-- aici deja știm că inputul este ok    

def cube(number):
    power = number ** 3
    return power

print("Cubul numarului {number} este {cube}".format(
                            number=v,
                            cube=cube(v))
)


print(f"Cubul numarului {v} este {cube(v)}")


#8. printați toate numerele întregi de la 100 la 124
# folosind `for` și `range()`

for x in range(100, 125):
    print(x)


#9. printați toate numerele întregi de la 100 la 124,
# folosind while.
x = 100
while x < 125:
    print(x)
    x += 1

 
#10. scrieți o funcție ce calculează factorialul unui număr.
# factorialul unui nr. întreg pozitiv `n` este egală cu
# produsul tuturor numerelor întregi din intervalul [1, n].


def factorial(n):
    # pattern de acumulare
    f = 1

    for x in range(1, n+1):
        f *= x

    return f

#11. scrieți o funcție ce calculează taxa de livrare pentru o comandă,
# pe baza distanței de livrare și a greutății pachetului,
# conform următoarelor specificații:
# - pt. distanțe < 10km:
#   - pt. pachete < 5kg: 5€
#   - pt. pachete >= 5kg: 8€
# - pt. distanțe >= 10km:
#   - pt. pachete < 5kg: 10€
#   - pt. pachete >= 5kg: 15€

def tax(distance, weight):
    if distance < 10:
        delivery = 5 if weight < 5 else 8
    else:
        delivery = 10 if weight < 5 else 15
    
    return delivery


def tax(distance, weight):
    # don't do this
    return (
        5 if weight < 5 else 8
    ) if distance < 10 else (
        10 if weight < 5 else 15
    )


# 12. scieți o funcție `is_leap_year(year)` ce returnează bool.
#
# un an bisect:
# a) este divizibil cu 4, dar
# b) nu este divizibil cu 100,
# c) decât dacă este totuși divizibil cu 400.
#
# testați funcția pe anii 2020, 2021, 2022, 2000, 1900

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False

def is_leap_year(year):
    return (
        year % 4 == 0 # divisible by 4
        and
        (
            year % 100 != 0 # but not divisible by 100
            or
            year % 400 == 0 # unless divisible by 400
        )
    )

for year in 2020, 2021, 2022, 2000, 1900:
    print(year, is_leap_year(year))


#13. scrieți o funcție `common_elements(iter1, iter2)`
# ce primește ca parametri două iterabile,
# și returnează o listă cu elementele comune.
#
# (intersecția a două mulțimi)

def common_elements(iter1, iter2):
    list = []
    for x in iter1:
        for y in iter2:
            if x == y:
                list.append(x)
                break
    return list


def common_elements(iter1, iter2):
    list = []
    for x in iter1:
        if x in iter2:
            list.append(x)
    return list




            