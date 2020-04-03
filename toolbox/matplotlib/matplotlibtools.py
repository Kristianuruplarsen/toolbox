
''' General tools for working with matplotlib
'''

import numpy as np
from functools import wraps
import matplotlib.pyplot as plt 

def integer_ticks(data, spacing = 1):
    ''' Construct integer tick labels from 
        a sequence of data.
    '''
    return np.arange(np.floor(np.min(data)),
                     np.ceil(np.max(data)) + 1,
                     spacing)


def adjust_spines(ax, spines = ['left', 'bottom']):
    ''' Adjust the spines of an axis to have 
        spacing between them where they meet.
    '''
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none')
    
    if 'left' in spines:
        ax.yaxis.set_tick_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_tick_position('bottom')
    else:
        ax.xaxis.set_ticks([])


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