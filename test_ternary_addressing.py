import unittest
from ternary_addressing import to_ternary

class TestTernaryAddressing(unittest.TestCase):

    def test_to_ternary(self):
        self.assertEqual(to_ternary(0), "00000000")
        self.assertEqual(to_ternary(1), "00000001")
        self.assertEqual(to_ternary(2), "00000002")
        self.assertEqual(to_ternary(3), "00000010")

if __name__ == '__main__':
    unittest.main()
