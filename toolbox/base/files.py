
''' Tools for working with files
'''

import pickle

def to_pickle(object, filename):
    ''' Save an object in pickle format.

    Parameters
    ----------
    object (any): A python object to serialize.
    filename (str): The name of the pickle file 
                    to save.

    Returns
    -------
    None
    '''
    with open(filename, "wb") as f:
        pickle.dump(object, f)


def from_pickle(filename):
    ''' Load an object in pickle format.

    Parameters
    ----------
    filename (str): The name of the pickle file 
                    to save.
                    
    Returns
    -------
    Object
    '''
    with open(filename, 'rb') as f:
        return pickle.load(f)
