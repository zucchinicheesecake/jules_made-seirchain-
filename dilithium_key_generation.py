from pqcrypto.sign.dilithium3 import keypair

def generate_dilithium_key():
    """
    Generates a Dilithium key pair.
    """
    return keypair()

if __name__ == '__main__':
    pk, sk = generate_dilithium_key()
    print(f"Public key: {pk}")
    print(f"Secret key: {sk}")
