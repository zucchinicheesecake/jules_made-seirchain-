import unittest
from serialization import serialize_triad

class MockTriad:
    def to_dict(self):
        return {"a": 1}

class TestSerialization(unittest.TestCase):

    def test_serialize_triad(self):
        triad = MockTriad()
        serialized_triad = serialize_triad(triad)
        self.assertEqual(serialized_triad, b'{"a": 1}')

if __name__ == '__main__':
    unittest.main()
