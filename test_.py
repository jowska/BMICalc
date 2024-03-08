import bmi
import unittest
from unittest.mock import patch

class Test_GetHeightInp(unittest.TestCase):
    @patch('builtins.input', return_value='5, 11')
    def test_typical_value(self, mock_input):
        result = bmi.get_height_inp()
        self.assertEqual(result, '5, 11')

class Test_SplitInp(unittest.TestCase):
    def test_typical_value(self):
        assert bmi.split_inp("6, 0") == ("6", "0")

    def test_no_space(self):
        assert bmi.split_inp("6,0") == ("6", "0")

    def test_empty_string(self):
        assert bmi.split_inp("") == ("", "")

class Test_CalcHeightAsInches(unittest.TestCase):
    def test_typical_value(self):
        assert bmi.calc_height_in_inches('5', '11') == 71

    def test_zero_value(self):
        assert bmi.calc_height_in_inches('0', '0') == 0

    def test_neg_value(self):
        assert bmi.calc_height_in_inches('-1', '-1') == 1

    def test_large_value(self):
        assert bmi.calc_height_in_inches('1000', '1000') == 12012

class Test_CalcHeightAsMeters(unittest.TestCase):
    def test_typical_value(self):
        assert bmi.calc_height_in_meters(71) == 1.8034

    def test_large(self):
        assert bmi.calc_height_in_meters(10000) == 254

    def test_neg(self):
        assert bmi.calc_height_in_meters(-100) == -2.54

class Test_GetWeightInp(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_get_weight_inp(self, mock_input):
        result = bmi.get_weight_inp()
        self.assertEqual(result, "100")

class Test_CalcWeightAsKg(unittest.TestCase):
    def test_typical_value(self):
        assert bmi.calc_weight_in_kg(154) == 69.853168

    def test_large(self):
        assert bmi.calc_weight_in_kg(90000) == 4082.331

    def test_neg(self):
        assert bmi.calc_weight_in_kg(-154) == -69.853168

class Test_CalculateBMI(unittest.TestCase):
    def test_typical(self):
        assert bmi.calculate_bmi(1.8034,69.853168) == 21.4784024886439

    def test_neg(self):
        assert bmi.calculate_bmi(-1.8034,-69.853168) == -21.4784024886439
    
    def test_zero(self):
        assert bmi.calculate_bmi(0,0) == 0

class Test_FindBMILabel(unittest.TestCase):
    def test_typical(self):
        assert bmi.find_bmi_label(21.4784024886439) == 'Normal weight'

    def test_neg(self):
        assert bmi.find_bmi_label(-21.4784024886439) == 'Underweight'

if __name__ == '__main__':
    unittest_main()