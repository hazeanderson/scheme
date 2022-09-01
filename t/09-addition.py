import unittest
from schemer.chapter02 import( tup )
from schemer.chapter04 import( add1, sub1, plus, minus )


class TestLoad(unittest.TestCase):

    def test_add1(self):
        self.assertEqual( add1(41), 42, '41 + 1 = 42' )
        self.assertEqual( add1('atom'), 0, 'atom + 1 = ?' )
        self.assertEqual( add1(None), 0, 'None + 1 = ?' )

    def test_sub1(self):
        self.assertEqual( sub1(43), 42, '43 - 1 = 42' )
        self.assertEqual( sub1('atom'), 0, 'atom + 1 = ?' )
        self.assertEqual( sub1(None), 0, 'None + 1 = ?' )

    def test_plus(self):
        self.assertEqual( plus(20, 22), 42, '20 plus 22 equals 42' )
        # TODO address these
        self.assertEqual( plus(20, 'atom'), 20, 'atom + 1 = ?' )
        self.assertEqual( plus(20, None), 20, 'None + 1 = ?' )

    def test_minus(self):
        self.assertEqual( minus(20, 22), -2, '20 minus 22 equals -2' )
        # TODO address these
        self.assertEqual( minus(20, 'atom'), 20, 'atom + 1 = ?' )
        self.assertEqual( minus(20, None), 20, 'None + 1 = ?' )


    #TODO move to chapter 1
    def test_tup(self):
        self.assertEqual( tup([1,2,3]), True, '[1,2,3] is a tup' )
        self.assertEqual( tup([1,'atom',3]), False, '[1,atom,3] is not a tup' )
        self.assertEqual( tup(1), False, '1 is not a tup' )



if __name__ == '__main__':
    unittest.main(verbosity=3)
