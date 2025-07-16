import unittest
from address_generation import generate_address

class TestAddressGeneration(unittest.TestCase):

    def test_generate_address(self):
        public_key = b"test_public_key"
        address = generate_address(public_key)
        self.assertEqual(address, "e5df42b01eefa2dd8a4485cc1978af05c8268e75b40a5bcde6afc3c4e785a2d0")

if __name__ == '__main__':
    unittest.main()
