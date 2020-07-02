import unittest
from Calculator.Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squared_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareroot_method_calculator(self):
        test_data = CsvReader('/src/Unit_Test_Square_Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']), 7))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 7))

if __name__ == '__main__':
    unittest.main()