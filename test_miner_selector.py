import unittest
import os
from miner_selector import MinerSelector

class TestMinerSelector(unittest.TestCase):

    def test_miner_selection(self):
        secret_key = os.urandom(32)
        miners = ["Alice", "Bob", "Charlie", "David"]
        seed = b"seed"
        selector = MinerSelector(secret_key)

        # Test miner selection
        selected_miner, proof = selector.select_miner(miners, seed)
        self.assertIn(selected_miner, miners)

        # Test verification
        self.assertTrue(selector.verify_miner_selection(proof, seed, selected_miner, miners))

        # Test invalid verification
        self.assertFalse(selector.verify_miner_selection(proof, seed, "Eve", miners))

if __name__ == '__main__':
    unittest.main()
