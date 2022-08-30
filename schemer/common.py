__version__='0.0.1'

# s_expr is an atom
def atom(s_expr):
    return not isinstance(s_expr, list) and s_expr is not None

# lat is empty
def null(lat):
    return isinstance(lat, list) and not len(lat) and lat is not None

# construct new lat with at and lat
def cons(at, lat):
    new_list = lat.copy()
    new_list.insert(0, at)
    return new_list

# return first atom in lat
def car(s_expr):
    if not atom(s_expr):
        return s_expr[0]

# return all of lat without its first atom
def cdr(lat):
    new_list = lat.copy()
    if new_list:
        new_list.pop(0)
    return new_list

# s_expr is a lat
def lat(s_expr):
    if null(s_expr):
        return True
    elif atom(car(s_expr)):
        return lat(cdr(s_expr))
    else:
        return False

# lat contains at least one occurance of a
def member(at, lat):
    if null(lat):
        return False
    else:
        return car(lat) == at or member(at, cdr(lat))

# remove first occurance of a from lat
def rember(a, lat):
    if null(lat):
        return []
    elif car(lat) == a:
        return cdr(lat)
    else:
        return cons(car(lat), rember(a, cdr(lat)))

# return new lat containing first elements from lat's lats
def firsts(lat):
    if null(lat):
        return []
    else:
        return cons(car(car(lat)), firsts(cdr(lat)))

# insert new atom into lat, to the left of first occurance of old
def insertL(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cons(old, cdr(lat)))
    else:
        return cons(car(lat), insertL(new, old, cdr(lat)))

# insert new atom into lat, to the right of first occurance of old
def insertR(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(old, cons(new, cdr(lat)))
    else:
        return cons(car(lat), insertR(new, old, cdr(lat)))

# replace first occurance of old in lat with new
def subst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst(new, old, cdr(lat)))

# replace first occurance of o1 or 2 in lat with new
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
def multirember(a, lat):
    if null(lat):
        return []
    elif car(lat) == a:
        return multirember(a, cdr(lat))
    else:
        return cons(car(lat), multirember(a, cdr(lat)))

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
        return cons(car(lat), cons(new, multiinsertR(new, old, cdr(lat))))
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




