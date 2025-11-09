import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.as_tuple()}"

    def __str__(self):
        return str(self.as_tuple())
    
    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()
    
    def translate(self, x=0, y=0):
        self.x += x
        self.y += y

    @property
    def distance_from_origin(self):
        return self.distance_between(self, Point(0, 0))

    @staticmethod
    def distance_between(a, b):
        "computes the distance between two points"
        return math.sqrt(
            (a.x - b.x) ** 2 +
            (a.y - b.y) ** 2
        )


class ThreeDPoint(Point):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def as_tuple(self):
        return self.x, self.y, self.z


# =======================================

# Exercițiu:
# Știind că:
# - un context manager este o instanță a unei clase,
# - ce are implementate metodele
def __enter__(self):
    pass

def __exit__(self, exc_type, exc_val, exc_tb):
    pass

# scrieți un context manager TimeIt,
# ce face output nr.-ului de secunde petrecute
# în execuția blocului de cod din interiorul
# c.m.-ului (adică ce se găsește în `with ...`)

import time

class TimeIt:
    #def __init__(self):
    #    print("»", "entering __init__")

    def __enter__(self):
        #print("»", "entering __enter__")

        self._start = time.time()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("»", "entering __exit__")

        delta = time.time() - self._start

        print(f"Execution took {delta} seconds.")


# time.time() - time.time() # --> float
# datetime.datetime.now() - datetime.datetime.now() # datetime.timedelta

"""
with open("file.txt", "w") as f:
    print(f)
"""

ti = TimeIt()
print("outside: ti is", ti)


with ti as myti:
    #print("starting")
    print("inside: myti is", myti)

    time.sleep(3)
    #print("done")

