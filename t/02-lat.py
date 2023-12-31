import unittest
from schemer.primitives import lat

class TestLoad(unittest.TestCase):

    def test_lat(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( lat(mylist), True, 'lat is a lat' )
        self.assertEqual( lat(['a','b','c']), True, 'lat is a lat' )
        self.assertEqual( lat(['a',None,'c']), False, 'lat with empty element is not a lat' )
        self.assertEqual( lat(['a',mylist,'c']), False, 'lat that contains another list is not a lat' )
        self.assertEqual( lat('not a list'), False, 'atom is not a lat' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main(verbosity=2)
