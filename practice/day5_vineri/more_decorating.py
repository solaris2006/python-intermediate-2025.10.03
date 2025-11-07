# ok, let's decorate

# Exercițiu:
# scrieți o funcție 
def timeit(func):
    pass

# ce primește ca parametru o altă funcție,
# o rulează fără argumente, și înainte
# de a returna rezultatul execuției
# face print la stderr cu durata execuției.

from time import sleep
def my_sleepy():
    print("i am the regular func")
    sleep(2)
    print("regular func done")

    return "a return value"

import datetime
import sys

def timeit(func):
    start = datetime.datetime.now()
    result = func()
    end = datetime.datetime.now()

    duration = end - start

    print("» exec:", duration, file=sys.stderr)

    return result

# Exercițiu:
# transformați funcția timeit, astfel încât să primească
# argumentele adiționale *args și **kwargs.
#
# pasați aceste argumente execuției lui func.
# modificați my_sleepy să primească argumentele x, y=None

def my_sleepy(x, y=None):
    "eu sunt o funcție care nu fac mare lucru"

    print("i am the regular func")
    print("executată cu x:", x, "y:", y)
    sleep(2)
    print("regular func done")

    return "a return value" * x


def timeit(func, *args, **kwargs):
    start = datetime.datetime.now()
    result = func(*args, **kwargs)
    end = datetime.datetime.now()

    duration = end - start

    print("» exec:", duration, file=sys.stderr)

    return result

# Exercițiu:
# Idee nouă 💡 !
# modificăm `timeit`
# astfel încât:
# 1) să primească un singur parametru o funcție
#    (facem revert la semnătura inițială)
# 2) în interiorul ei va defini o funcție
def inner(*args, **kwargs):
    # ...
    pass
# 3) mutăm logica de timing și execuție a lui `func`
#    în interiorul lui `inner()`
# 4) returnăm din `timeit` pe `inner`

from functools import wraps
def timeit(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        
        # we are agnostic about the func's arguments,
        # and we are agnostic about its return value.

        # all we do, is execute it with the normally given args and kwargs
        result = func(*args, **kwargs)
        
        end = datetime.datetime.now()

        duration = end - start

        print("» exec:", duration, file=sys.stderr)

        return result
    
    return inner

# în momentul ăsta a devenit decorator
# înseamnă că primește argument o funcție
# și returnează o altă funcție

replaced_sleepy = timeit(my_sleepy) # data type? function!

# help(replaced_sleepy)
# --> numele ei este "inner"
# --> are semnătură (*args, **kwargs)

@timeit
def my_sleepy(x, y=None):
    "eu sunt o funcție care nu fac mare lucru"

    print("i am the regular func")
    print("executată cu x:", x, "y:", y)
    sleep(2)
    print("regular func done")

    return "a return value" * x



def myfunc():
    return myotherfunc()

print("fac ceva")

def myotherfunc():
    return 42


# Exercițiu

# știind că există metoda specială
def __call__(self):
    print("eu mă rulez")
# (adică putem crea obiecte callable)

# haideți să facem o clasă decorator TimeIt


class TimeIt:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        
        # we are agnostic about the func's arguments,
        # and we are agnostic about its return value.

        # all we do, is execute it with the normally given args and kwargs
        result = self.func(*args, **kwargs)
        
        end = datetime.datetime.now()

        duration = end - start

        print("» exec:", duration, file=sys.stderr)

        return result



obj = TimeIt()
callable(obj) # True


# definiția veche a decoratorului:
#   "o funcție care returnează o funcție"

# definiția nouă a decoratorului:
#   "un callable care returnează un callable"



@TimeIt
def my_sleepy(x, y=None):
    "eu sunt o funcție care nu fac mare lucru"

    print("i am the regular func")
    print("executată cu x:", x, "y:", y)
    sleep(2)
    print("regular func done")

    return "a return value" * x












