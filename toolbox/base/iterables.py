
''' Tools for working with iterables in base python 
'''

from collections.abc import Iterable


# -------------------------------------------
# Tools for iterables
# -------------------------------------------

def flatten(items):
    ''' Yield items from a nested iterable.

    Parameters
    ----------
    items (iterable): a nested iterable structure.

    Returns
    -------
    generator
    '''
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


