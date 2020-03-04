
''' Tools for working with strings
'''


from functools import wraps

def remove_or_replace_symbols(s, symbols, replacement = ''):
    ''' Remove or replace symbols from a string.

    Parameters
    ----------
    s (str): string to remove symbols from.
    symbols (str/list): (list of) symbols to remove.
    replacement (str): what to replace the symbols with. 
                      Default is nothing ''.
    
    Returns
    -------
    String
    '''
    if isinstance(symbols, str):
        symbols = (symbols,)

    for sym in symbols:
        s = s.replace(sym, replacement)    
    
    return s


def make_remover(symbols, name = None):
    if name is None:
        name = ','.join(symbols)
    docs = f''' Remove {name} from a string.

        Params
        ------
        s (str): String with {name} to remove

        Returns
        -------
        string
        '''    
    def _remover(s):
        return remove_or_replace_symbols(s, symbols, '') 
    _remover.__doc__ = docs
    return _remover

remove_parenthesis = make_remover(('(', ')'), 'parenthesis')
remove_backets = make_remover(('[', ']'), 'brackets')
remove_curly = make_remover(('{', '}'), 'curly braces')


