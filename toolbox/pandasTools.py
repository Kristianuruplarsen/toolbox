
""" These are utility functions designed to work with the pandas module.
"""

import pandas as pd


def gather(df, key, value, cols):
    """ Convert from wide to long format data with the same syntax as in R.
    """
    id_vars = [ col for col in df.columns if col not in cols ]
    id_values = cols
    var_name = key
    value_name = value
    return pd.melt( df, id_vars, id_values, var_name, value_name )


def spread(df, key, value):
    """ Convert from long to wide format with the same syntax as in R.
    """
    cols = [col for col in df.columns if col not in (key, value)]
    return pd.pivot_table(df, index = cols, columns = key, values = value)\
            .reset_index()
