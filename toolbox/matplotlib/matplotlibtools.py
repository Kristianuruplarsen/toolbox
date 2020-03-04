
''' General tools for working with matplotlib
'''


from functools import wraps
import matplotlib.pyplot as plt 


def logx(plot_function):
    ''' Use logarithmic x scale.
    '''
    @wraps(logx)
    def _wrapped():
        out = plot_function()
        plt.xscale('log')
        return out
    return _wrapped


def logy(plot_function):
    ''' Use logarithmic x scale.
    '''
    @wraps(logy)
    def _wrapped():
        out = plot_function()
        plt.yscale('log')
        return out
    return _wrapped