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

