import unittest
import pandas as pd
import Transform as tr 

class TestTemperatureConversion(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        # Test for normal temperature conversion
        self.assertAlmostEqual(tr.kelvin_to_celsius(300), 26.85, places = 2)
        
        # Test for absolute zero (0 Kelvin)
        self.assertAlmostEqual(tr.kelvin_to_celsius(0), -273.15, places = 2)
        
        # Test for negative temperature in Kelvin
        self.assertAlmostEqual(tr.kelvin_to_celsius(-50), -323.15, places = 2)

if __name__ == '__main__':
    unittest.main()
