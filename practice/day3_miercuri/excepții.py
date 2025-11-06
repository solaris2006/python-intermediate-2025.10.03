# excepții

import ipdb # pip install ipdb


l = [1, 2, 3]
d = {}
try:
    v = l[2] / 1
    d[v]
    print(
        l[2] / 0
    )

except ZeroDivisionError:
    print("exception: zero div")

except IndexError:
    print("exception: index error")

except Exception as e:
    print("exception: catch-all situation")
    print("will proably log `e`", type(e), e.args)

else:
    # se rulează dacă nu a existat excepție
    print("O.K.: totul în regulă")

finally:
    # se rulează __întotdeauna__
    print("finally: aici poate vreau să fac cleanup")


print("final")