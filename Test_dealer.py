import unittest
from dealer import Vehicle
from dealer import tax

test_car = Vehicle("2020", "Toyota", "GR Supra", "RZ", str(3.0), "1540kg", "170g/km", "Red", "¥7027778")

class Testtax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
    
    def setUp(self):
        print('setUp')
        self.tax = tax(car.price.strip('¥'))
    
    def tearDown(self):
        print('teardown\n')
    
    def test_environment_tax(self):
        print("test_environment_tax")
        self.assertEqual(self.tax.environment_tax, 50000)

if __name__ == '__main__':
    unittest.main()