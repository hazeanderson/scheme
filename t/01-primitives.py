import unittest
from schemer.primitives import( atom, null, cons, car, cdr )


class TestLoad(unittest.TestCase):

    def test_atom(self):
        self.assertEqual( atom(['a','b','c']), False, 'list is not an atom' )
        self.assertEqual( atom(None), False, 'None is not an atom' )
        self.assertEqual( atom('atom'), True, 'atom is an atom' )
        self.assertEqual( atom('turkey'), True, 'atom is an atom' )
        self.assertEqual( atom('*abc$'), True, 'atom is an atom' )

    def test_null(self):
        self.assertEqual( null(['a','b','c']), False, 'lists are not null' )
        self.assertEqual( null('atom'), False, 'atoms are not null' )
        self.assertEqual( null([]), True, 'empty list is null' )

    def test_cons(self):
        mylist = ["banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( cons('apple', mylist), ["apple", "banana", "cherry"], 'cons atom onto lat' )
        self.assertEqual( cons(mylist, mylist), [["banana", "cherry"], "banana", "cherry"], 'car lat onto lat' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_car(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( car('mylist'), None, 'car of atom is none' )
        self.assertEqual( car(mylist), 'apple', 'car return 1st element' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_cdr(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( cdr(mylist), ["banana", "cherry"], 'cdr return rest of list' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main(verbosity=2)
