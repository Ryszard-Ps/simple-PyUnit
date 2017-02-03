import unittest

from should_dsl import should

from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):
    def test_suma(self):
        Calculadora.suma(12,5) | should | equal_to(17)

if __name__ == '__main__':
    unittest.main
