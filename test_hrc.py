import unittest
from hrc import hrc_finality

class MockTriad:
    def __init__(self):
        self.children = []

class TestHRC(unittest.TestCase):

    def test_hrc_finality(self):
        root = MockTriad()
        child1 = MockTriad()
        child2 = MockTriad()
        root.children = [child1, child2]

        child1_1 = MockTriad()
        child1.children = [child1_1]

        child1_1_1 = MockTriad()
        child1_1.children = [child1_1_1]

        self.assertTrue(hrc_finality(root))

        child1_1_1.children = [MockTriad()]
        self.assertTrue(hrc_finality(root))

if __name__ == '__main__':
    unittest.main()
