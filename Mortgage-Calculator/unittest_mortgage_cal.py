import unittest
from unittest.mock import patch
import sys
import io
import math
from calculator_app import property_price, mort_duration, interest_rate, initial_payment, calculate_monthly_payment

class TestMortgageCalculator(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements during tests
        self.held_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Restore stdout after each test
        sys.stdout = self.held_stdout
        

    @patch('builtins.input', return_value='300000')
    def test_property_price_valid(self, mock_input):
        self.assertEqual(property_price(), 300000)

    @patch('builtins.input', side_effect=['90000', '150000'])
    def test_property_price_invalid_then_valid(self, mock_input):
        self.assertEqual(property_price(), 150000)

    @patch('builtins.input', return_value='20')
    def test_mort_duration_valid(self, mock_input):
        self.assertEqual(mort_duration(), 20)

    @patch('builtins.input', side_effect=['-5', '35', '15'])
    def test_mort_duration_invalid_then_valid(self, mock_input):
        self.assertEqual(mort_duration(), 15)

    @patch('builtins.input', return_value='5.5')
    def test_interest_rate_valid(self, mock_input):
        self.assertEqual(interest_rate(), 0.055)

    @patch('builtins.input', side_effect=['-3', '4.2'])
    def test_interest_rate_invalid_then_valid(self, mock_input):
        self.assertEqual(interest_rate(), 0.042)

    @patch('builtins.input', return_value='50000')
    def test_initial_payment_valid(self, mock_input):
        self.assertEqual(initial_payment(), 50000)

    @patch('builtins.input', side_effect=['-1000', '25000'])
    def test_initial_payment_invalid_then_valid(self, mock_input):
        self.assertEqual(initial_payment(), 25000)

    def test_calculate_monthly_payment(self):
        # Test with known values
        price = 300000
        duration = 30
        interest = 0.05
        down_payment = 60000
        expected_payment = round(240000 * ((0.05 / 12 * (1 + 0.05 / 12) ** (30 * 12)) / ((1 + 0.05 / 12) ** (30 * 12) - 1)))
        self.assertEqual(round(calculate_monthly_payment(price, duration, interest, down_payment)), expected_payment)


if __name__ == '__main__':
    unittest.main()
