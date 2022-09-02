__version__='0.0.1'
from schemer.primitives import( null, car, cdr )

# lat contains at least one occurance of a
def member(at, lat):
    if null(lat):
        return False
    elif car(lat) == at:
        return True
    else:
        return member(at, cdr(lat))

