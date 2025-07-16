from concurrent.futures import ThreadPoolExecutor

def verify_triad_batch(triads):
    """
    Verifies a batch of Triads in parallel.
    """
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda t: t.verify(), triads))
    return all(results)
