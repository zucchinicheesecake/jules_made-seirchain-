import json

def serialize_triad(triad):
    """
    Serializes a Triad object.
    """
    return json.dumps(triad.to_dict(), sort_keys=True).encode()
