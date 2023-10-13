import unittest
import subprocess

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = subprocess.check_output(['python', 'calculator.py', '1', '2', '3'])
        self.assertEqual(result.strip(), b'Sum : 2.0 + 3.0 = 5.0')

    def test_subtraction(self):
        result = subprocess.check_output(['python', 'calculator.py', '2', '6', '3'])
        self.assertEqual(result.strip(), b'Substraction : 6.0 - 3.0 = 3.0')

    def test_multiplication(self):
        result = subprocess.check_output(['python', 'calculator.py', '3', '4', '5'])
        self.assertEqual(result.strip(), b'Multiplication : 4.0 x 5.0 = 20.0')

    def test_division(self):
        result = subprocess.check_output(['python', 'calculator.py', '4', '12', '4'])
        self.assertEqual(result.strip(), b'DIvision : 12.0 / 4.0 = 3.0')

    def test_div_by_zero(self):
        result = subprocess.check_output(['python', 'calculator.py','4','1','0'])
        self.assertEqual(result.strip(),b'Cannot divide by 0')
    def runTest(self):
        test_addition(self)

        test_subtraction(self)

        test_multiplication(self)

        test_division(self)

        test_div_by_zero(self)

if __name__ == '__main__':
    unittest.main()

