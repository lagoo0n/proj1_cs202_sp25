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
        rc = RegionCondition(Region(GlobeRect(35.0, 35.6, -120.9, -120.2), "San Luis Obispo", "other"), 2025, 300000, 500000.0)
        self.assertAlmostEqual(emissions_per_capita(rc), 500000.0 / 300000)

    def test2_emissions_per_capita(self):
        rc = RegionCondition(Region(GlobeRect(35.0, 35.6, -120.9, -120.2), "San Luis Obispo", "other"), 2025, 0, 100000000.0)
        self.assertAlmostEqual(emissions_per_capita(rc), 0.0)

    def test_area(self):
        gr = GlobeRect(10.0, 20.0, 30.0, 40.0)
        self.assertAlmostEqual(area(gr), 1195445.55)

    def test_emissions_per_square_km(self):
        rc = RegionCondition(Region(GlobeRect(10.0, 20.0, 30.0, 40.0), "San Luis Obispo", "other"), 2025, 1000, 5000.0)
        self.assertAlmostEqual(emissions_per_square_km(rc), 5000.0 / 1195445.55)

    def test_densest(self):
        rc = [RegionCondition(Region(GlobeRect(10.0, 20.0, 30.0, 40.0), "Region1", "other"), 2025, 1000, 5000.0),
                   RegionCondition(Region(GlobeRect(10.0, 20.0, 30.0, 40.0), "Region2", "other"), 2025, 2000, 10000.0),
                   RegionCondition(Region(GlobeRect(10.0, 20.0, 30.0, 40.0), "Region3", "other"), 2025, 3000, 100000.0)]
        self.assertEqual(densest(rc), "Region3")


if __name__ == '__main__':
    unittest.main()
