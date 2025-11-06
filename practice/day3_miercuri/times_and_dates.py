# times and dates

# modulul time: utilitare, more low-level, legacy
import time
time.sleep(2)
time.time() # 1970-01-01 00:00:00

# modulul datetime: structuri pythonice
import datetime
datetime.date # se ocupă cu zile
datetime.time # se ocupă cu ore-minute-secunde-microsecunde
datetime.datetime # se ocupă cu fully-qualified timestamp
datetime.timedelta # o diferență de timpi

datetime.date(2025, 11, 7)
day_after_tomorrow = datetime.date(2025, 11, 7)

datetime.date.today() # classmethod
today = datetime.date.today() # classmethod

datetime.datetime.now()
now = datetime.datetime.now()

day_after_tomorrow - today # timedelta object

new_now = datetime.datetime.now()

delta = new_now - now # timedelta object

# useful:
delta.total_seconds()


# Exercițiu:
# calculați durata de execuție a următoarei bucăți de cod:

import time
import datetime

# start timing
start_dt = datetime.datetime.now()
start_t = time.time()

with open("open_docs.txt") as fp:
    for line in fp:
        if "read" in line:
            print(line, end="")

# end timing
end_dt = datetime.datetime.now()
end_t = time.time()

print("timedelta obj", end_dt - start_dt)
print("numeric", end_t - start_t)


# Exercițiu:
# Scrieți o funcție
def alarm(timespec, payload):
    pass
# unde `timespec` este un string de forma
# HH / HH:MM / HH:MM:SS
# și `payload` este o funcție ce va fi rulată
# la ora respectivă

def alarm(timespec, payload):
    parts = timespec.split(':')

    match len(parts):
        case 3:
            h, m, s = map(int, parts)
        case 2:
            h, m = map(int, parts)
            s = 0
        case 1:
            h, = map(int, parts)
            m, s = 0, 0
        case _:
            raise ValueError("Invalid timespec: '%s'" % timespec)
    # TODO: also raise in case of failing int() conversion

    print(h, m, s)

    # next:
    # 1) aflăm dacă acest timespec este azi sau mâine
    # 2) aflăm cât timp este între acum și atunci
    # 3) facem ceva cu acest timedelta. ce?

    # hint:
    # `datetime` objects have a `.replace()` method


