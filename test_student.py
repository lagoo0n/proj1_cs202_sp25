import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_holder(self):
        pass

    def test1_emissions_per_capita(self):
        region = RegionCondition(Region(GlobeRect(35.0, 35.6, -120.9, -120.2), "San Luis Obispo", "other"), 2025, 300000, 500000.0)
        self.assertAlmostEqual(emissions_per_capita(region), 500000.0 / 300000)

    def test2_emissions_per_capita(self):
        region = RegionCondition(Region(GlobeRect(35.0, 35.6, -120.9, -120.2), "San Luis Obispo", "other"), 2025, 0, 100000000.0)
        self.assertAlmostEqual(emissions_per_capita(region), 0.0)


if __name__ == '__main__':
    unittest.main()
