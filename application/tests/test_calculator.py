import unittest
import subprocess
import os

# Get the absolute path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        # Construct the command with the relative file path to calculator.py
        command = ['python', os.path.join(current_dir, '../calculator.py'), '1', '2', '3']
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = result.communicate()
        self.assertEqual(stdout.strip().decode('utf-8'), 'Sum : 2.0 + 3.0 = 5.0')

    def test_subtraction(self):
        # Construct the command with the relative file path to calculator.py
        command = ['python', os.path.join(current_dir, '../calculator.py'), '2', '6', '3']
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = result.communicate()
        self.assertEqual(stdout.strip().decode('utf-8'), 'Substraction : 6.0 - 3.0 = 3.0')

    def test_multiplication(self):
        # Construct the command with the relative file path to calculator.py
        command = ['python', os.path.join(current_dir, '../calculator.py'), '3', '4', '5']
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = result.communicate()
        self.assertEqual(stdout.strip().decode('utf-8'), 'Multiplication : 4.0 x 5.0 = 20.0')

    def test_division(self):
        # Construct the command with the relative file path to calculator.py
        command = ['python', os.path.join(current_dir, '../calculator.py'), '4', '12', '4']
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = result.communicate()
        self.assertEqual(stdout.strip().decode('utf-8'), 'DIvision : 12.0 / 4.0 = 3.0')

    def test_div_by_zero(self):
        # Construct the command with the relative file path to calculator.py
        command = ['python', os.path.join(current_dir, '../calculator.py'), '4', '1', '0']
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = result.communicate()
        self.assertEqual(stdout.strip().decode('utf-8'), 'Cannot divide by 0')

if __name__ == '__main__':
    unittest.main()

