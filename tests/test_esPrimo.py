import unittest
from Funciones import esPrimo

class TestEsPrimo(unittest.TestCase):

    def test_isANUmber(self):
        self.assertFalse(esPrimo("A"))
        self.assertFalse(esPrimo(True))
        self.assertFalse(esPrimo(3.4))
        self.assertTrue(esPrimo(11))


if __name__ == '__main__':
    unittest.main()
