# stringuri

# metode importante:

"""
.join() / .split() / .rsplit()


.strip() / .lstrip() / .rstrip()
.removeprefix() / .removesuffix()

.replace()

.lower() / .upper()

.startswith() / .endswith() 

.find() / .index()

.splitlines()

.center() / .ljust() / .rjust() / .zfill()

.count()

.format()


"""

# Exercițiu:
# dat fiind numele de coloană
c = "####Name####"
# obțineți numele de coloană fără caracterele
# de padding

c.strip("#")


# Exercițiu:
# dat fiind capul de tabel
h = "|####Name # etc####|#Age#|#####Address#####|"
# obțineți o listă cu numele coloanelor

# concepte atinse:
# split, cleanup, indecși, construcție de listă

cols = []
for col in h.split('|')[1:-1]:
    col = col.strip('#')
    cols.append(col)

print(cols)



# Exercițiu:
# scriem o funcție care replică funcționalitatea
# lui str.startswith()

def startswith(substr, txt):
    # returns bool
    return txt[:len(substr)] == substr



# Exercițiu:
# scriem o funcție care replică funcționalitatea
# lui str.removesuffix

def removesuffix(substr, txt):
    # returns a new string
    suffix = txt[-len(substr):] # obținem caracterele de la final 
    if substr == suffix:
        return txt[:-len(substr)]

    return txt

print(
    removesuffix("abc", "blabc blabc")
)

print(removesuffix("ta", "acesta"))


# transformați stringul
"00000124"
# într-un număr întreg
int("000001240".lstrip("0"))

# transformați int-ul
1240
# în str prefixat cu "0" până la 10 caractere
def padint(number, length):
    num_as_str = str(number)
    numchars = len(num_as_str)
    numzeros = length - numchars

    if numzeros <= 0:
        return num_as_str
    return "0" * numzeros + num_as_str

print(padint(1240, 10)) # "0000001240"
print(padint(12345, 5)) # "12345"
print(padint(12345, 2)) # "12345"
print(padint(12345, 6)) # "012345"


# variable interpolation (old-school)
"un placeholder: » %f « a fost aici și » %s « aici" % (20, "wow")

# new-school, string formatting
"un string cu » {} « placeholder și » {} « altul".format("ceva", 20)
"un string cu » {arg1} « placeholder și » {arg2} « altul".format("ceva", 20)
