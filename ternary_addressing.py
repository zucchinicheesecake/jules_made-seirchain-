import numpy as np

def to_ternary(index, length=8):
    """
    Converts an index to a ternary string.
    """
    return np.base_repr(index, base=3).zfill(length)

if __name__ == '__main__':
    for i in range(10):
        print(f"{i}: {to_ternary(i)}")
