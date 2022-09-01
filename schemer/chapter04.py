__version__='0.0.1'
#from schemer.primitives import( atom, null, cons, car, cdr )

def plus(n, m):
    if not isinstance(m, int):
        return n

    if m == 0:
        return n
    else:
        return add1(plus(n, sub1(m)))


def minus(n, m):
    if not isinstance(m, int):
        return n

    if m == 0:
        return n
    else:
        return sub1(minus(n, sub1(m)))


def add1(n):
    if isinstance(n, int):
        return n + 1
    else:
        return 0

def sub1(n):
    if isinstance(n, int):
        return n - 1
    else:
        return 0
