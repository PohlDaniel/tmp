from typing import Callable
from functools import reduce

def mal(x: int) -> Callable[[int], int]:
    def mal_x(y: int) -> int:
        return x * y
    return mal_x

def multipliziere_liste_funktional(xs: list, k: int) -> list:
    mal_k = mal(k)
    return list(map(mal_k, xs))

def multipliziere_liste_funktional2(xs: list, k: int) -> list:
   return list(map(lambda x: x * k, xs))

def multipliziere_liste_funktional2_python(xs: list, k: int) -> list:
   return [x * k for x in xs]

def groesser_als(xs: list, k: int) -> list:
    return list(filter(lambda x: x > k, xs))

def groesser_als_python(xs: list, k: int) -> list:
    return [x for x in xs if x > k]

def summe(xs: list) -> int:
    return reduce(lambda x1, x2: x1 + x2, xs, 0)

def anzahl_gerade(xs: list) -> int:
    return reduce(lambda x1, x2: x1 + 1, list(filter(lambda x: x % 2 == 0, xs)), 0)

def increment(x , y):
    return  x + 1

def anzahl_gerade2(xs: list) -> int:
 return reduce(increment, list(filter(lambda x: x % 2 == 0, xs)), 0)

def curry(prior, *additional):
    def curried(*args):
        return prior(*(args + additional))
    return curried

def foo(x: int, y: int, z: int):
    return x + y + z

def inner(func, u: list, v):
    if(func(v)) : 
        return u + [v] 
    else:
        return u 

def mein_filter_inner(func, xs : list) -> list:
    def inner(u: list, v):
        if(func(v)) : 
            return u + [v] 
        else:
            return u 
    return reduce(inner, xs, [])

def mein_filter(func, xs: list) -> list:
    return reduce(lambda x1, x2: x1 + [x2] if func(x2) else x1, xs, [])
