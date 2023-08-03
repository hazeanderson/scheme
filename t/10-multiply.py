import unittest
from schemer.chapter04 import( multiply )


class TestLoad(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual( multiply(5, 3), 15, '5 added to itself 3 times equals 15' )



if __name__ == '__main__':
    unittest.main(verbosity=2)
