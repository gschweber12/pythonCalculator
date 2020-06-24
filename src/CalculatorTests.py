import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        testData = CsvReader('Unit_Test_Addition.csv').data
        self.assertEqual(self.calculator.add(2,2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2,2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2,2), 4)
        self.assertEqual(self.calculator.result, 4)

if __name__ == '__main__':
    unittest.main()