import unittest
import networkx as nx
from rpsf import simulate_rpsf

class TestRPSF(unittest.TestCase):

    def test_simulate_rpsf(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (4, 6)])

        self.assertTrue(simulate_rpsf(G, 0, 6))
        with self.assertRaises(nx.NodeNotFound):
            simulate_rpsf(G, 0, 7)

if __name__ == '__main__':
    unittest.main()
