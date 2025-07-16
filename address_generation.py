import hashlib

def generate_address(public_key):
    """
    Generates a wallet address from a public key.
    """
    return hashlib.sha256(public_key).hexdigest()
