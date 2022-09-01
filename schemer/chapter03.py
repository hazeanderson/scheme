__version__='0.0.1'
from schemer.primitives import( atom, null, cons, car, cdr )

# remove first occurance of a from lat
def rember(at, lat):
    if null(lat):
        return []
    elif car(lat) == at:
        return cdr(lat)
    else:
        return cons(car(lat), rember(at, cdr(lat)))

# return new lat containing first elements from lat's lats
# silly example
def firsts(lolat):
    if null(lolat):
        return []
    else:
        return cons(car(car(lolat)), firsts(cdr(lolat)))

# insert new atom into lat, to the left of first occurance of target
def insertL(new, target, lat):
    if null(lat):
        return []
    elif car(lat) == target:
        return cons(new, cons(target, cdr(lat)))
    else:
        return cons(car(lat), insertL(new, target, cdr(lat)))

# insert new atom into lat, to the right of first occurance of target
def insertR(new, target, lat):
    if null(lat):
        return []
    elif car(lat) == target:
        return cons(target, cons(new, cdr(lat)))
    else:
        return cons(car(lat), insertR(new, target, cdr(lat)))

# replace first occurance of old in lat with new
def subst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst(new, old, cdr(lat)))

# replace first occurance of o1 or 2 in lat with new
# silly example
def subst2(new, o1, o2, lat):
    if null(lat):
        return []
    elif car(lat) == o1:
        return cons(new, cdr(lat))
    elif car(lat) == o2:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst2(new, o1, o2, cdr(lat)))

# remove all occurances of a from lat
def multirember(at, lat):
    if null(lat):
        return []
    elif car(lat) == at:
        return multirember(at, cdr(lat))
    else:
        return cons(car(lat), multirember(at, cdr(lat)))

# insert new atom into lat, to the left of all occurances of old
def multiinsertL(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cons(old, multiinsertL(new, old, cdr(lat))))
    else:
        return cons(car(lat), multiinsertL(new, old, cdr(lat)))

# insert new atom into lat, to the right of all occurances of old
def multiinsertR(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(old, cons(new, multiinsertR(new, old, cdr(lat))))
    else:
        return cons(car(lat), multiinsertR(new, old, cdr(lat)))

# replace all occurances of old in lat with new
def multisubst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, multisubst(new, old, cdr(lat)))
    else:
        return cons(car(lat), multisubst(new, old ,cdr(lat)))

