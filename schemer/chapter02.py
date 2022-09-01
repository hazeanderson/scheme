__version__='0.0.1'
from schemer.primitives import( atom, null, cons, car, cdr )

# TODO: move lat() and tup() to primitives
# s_expr is a lat
def lat(s_expr):
    if null(s_expr):
        return True
    elif atom(car(s_expr)):
        return lat(cdr(s_expr))
    else:
        return False

def tup(s_expr):
    if null(s_expr):
        return True
    elif isinstance(car(s_expr), int):
        return tup(cdr(s_expr))
    else:
        return False

# lat contains at least one occurance of a
def member(at, lat):
    if null(lat):
        return False
    elif car(lat) == at:
        return True
    else:
        return member(at, cdr(lat))

