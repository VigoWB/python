import unittest
from zadanie_3 import noc_normalna, noc_tropikalna

class MyTestCase(unittest.TestCase):
    def test_noc_tropikalna_good_set(self):
        result = noc_tropikalna([22.0, 23.0, 24.0, 25.0, 22.0, 21.0, 20.5])
        self.assertTrue(result)

    def test_noc_tropikalna_bad_set(self):
        result = noc_tropikalna([22.0, 19.0, 24.0, 25.0, 22.0, 21.0, 20.5])
        self.assertTrue(not result)

    def test_noc_tropikalna_edge_set(self):
        result = noc_tropikalna([20.1, 20.0, 20.2])
        self.assertTrue(result)

    def test_noc_normalna_good_set(self):
        result = noc_normalna([21.0, 22.0, 19.0])
        self.assertTrue(result)

    def test_noc_normalna_bad_set(self):
        result = noc_normalna([21.0, 22.0, 32.0])
        self.assertSTrue(not result)

    def test_noc_normalna_edge_set(self):
        result = noc_normalna([21.0, 20.0, 32.0])
        self.assertTrue(not result)

if __name__ == '__main__':
    unittest.main()