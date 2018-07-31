
""" These are various small utility functions for working with pickle
"""

import pickle

def toPickle(object, filename):
    """ Pickles a thing
    """
    with open(filename, "wb") as f:
        pickle.dump(object, f)


def fromPickle(filename):
    """ Unpickles a thing
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)
