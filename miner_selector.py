import hashlib
import hmac

class MinerSelector:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def select_miner(self, miners, seed):
        """
        Selects a miner from a list of miners using an HMAC-based scheme.
        """
        if not miners:
            return None

        # Generate a proof
        proof = hmac.new(self.secret_key, seed, hashlib.sha256).digest()

        # Select a miner based on the proof
        miner_index = int.from_bytes(proof, 'big') % len(miners)
        return miners[miner_index], proof

    def verify_miner_selection(self, proof, seed, miner, miners):
        """
        Verifies a miner selection.
        """
        # Generate the expected proof
        expected_proof = hmac.new(self.secret_key, seed, hashlib.sha256).digest()

        if proof != expected_proof:
            return False

        # Check if the selected miner is correct
        miner_index = int.from_bytes(proof, 'big') % len(miners)
        return miners[miner_index] == miner
