# decoratori

import random
from functools import cache

@cache
def myrand():
    return random.randint(1, 100)

# ^^ perfect echivalent cu:

def myrand():
    return random.randint(1, 100)
myrand = cache(myrand)


def myrand():
    return random.randint(1, 100)
_my_old_rand = myrand()
myrand = cache(myrand)

# funcția `cache` primește ca argument o funcție
# și returnează o funcție ("un callable")


# Exercițiu:
# scrieți o funcție
def myrand(min_value, max_value):
    pass

# ce returnează o valoare random între `min_value` și `max_value`.
# testați-o.
#
# apoi decorați-o cu @cache.
# testați-o. (cu diverse valori)

@cache
def myrand(min_value, max_value):
    return random.randint(min_value, max_value)


# un decorator este o funcție care:
# - primește ca argument o funcție
# - și returnează o (altă) funcție.

# reformulăm *corect*:
# un decorator este un callable care:
# - primește ca argument un callable
# - și returnează un (alt) callable.

# (callables întâlnite până acum: function; class.)


# Să scriem un decorator care loghează
# fiecare call al funcției pe care o decorează,
# împreună cu argumentele sale,
# și cu valoarea returnată

def printingdeco(func):
    # `innerfunc` va înlocui pe `func`
    # în afara acestui cod
    def innerfunc(*args, **kwargs):
        retval = func(*args, **kwargs)

        print("» log:", f'{func.__module__}.{func.__name__}', args, kwargs, retval)

        return retval

    return innerfunc


@printingdeco
def myfunc(a, b):
    return 42 + a + b

