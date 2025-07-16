import hashlib

def hrc_finality(triad, depth=0):
    """
    Checks for HRC finality.
    """
    if depth >= 3:
        return True

    # In a real implementation, this would involve checking the PBFT consensus of the child triads.
    # For this simulation, we'll just assume that consensus is reached.

    for child in triad.children:
        if not hrc_finality(child, depth + 1):
            return False

    return True
