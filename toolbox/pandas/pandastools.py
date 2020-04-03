
''' Tools for working with pandas datasets
'''

import pandas as pd


def gather(df, key, value, cols):
    ''' Convert from wide to long format data with the same syntax as in R.

    Parameters
    ----------
    df (pd.DataFrame): a dataframe to gather to long format.
    key (str): name of key column to create
    value (str): name of value column to create
    cols (str): columns to gather.

    Returns
    -------
    pd.DataFrame
    '''
    id_vars = [ col for col in df.columns if col not in cols ]
    id_values = cols
    var_name = key
    value_name = value
    return pd.melt( df, id_vars, id_values, var_name, value_name )


def spread(df, key, value):
    ''' Convert from long to wide format with the same syntax as in R.

    Parameters
    ----------
    df (pd.DataFrame): a dataframe to spread to wide format.
    key (str): name of key column
    value (str):name of value column

    Returns
    -------
    pd.DataFrame
    '''
    cols = [col for col in df.columns if col not in (key, value)]
    return pd.pivot_table(df, index = cols, columns = key, values = value)\
            .reset_index()



class Collapse:
    def __init__(self, df, groups, funcs, columns = None):
        ''' Context manager that collapses a pd.DataFrame
            e.g. for plotting.

        Parameters
        ----------
        df (pd.DataFrame): the data to collapse.
        groups (list): the columns to group by.
        funcs (list): the functions to summarize by.
        columns (list): the columns to keep in the collapse.
        '''
        if isinstance(df, pd.DataFrame):
            self.df = df 
        if isinstance(df, pd.Series):
            self.df = df.reset_index()

        self.groups = self.set_groups(groups)
        self.funcs = self.set_functions(funcs)
        self.columns = self.set_columns(columns) if columns is not None else df.columns

        def _set(self, value, error = ''):
            if isinstance(value, list):
                return value 
            elif isinstance(value, tuple):
                return list(value)
            elif isinstance(value, str):
                return [x.strip() for x in value.split(',')]
            raise ValueError(error)

        def set_groups(self, groups):
            return self._set(groups, f'Unknown group format {groups}')

        def set_columns(self, columns):
            return self._set(columns, f'Unknown column format {columns}')

        def set_functions(self, funcs):
            return self._set(funcs, f'Unknown function format {funcs}')

        def __enter__(self):
            df = self.df.groupby(self.groups)[self.columns].agg(self.funcs).reset_index()
            df.columns = ['_'.join([a,b]) if b != '' else a for a,b in zip(df.columns.get_level_values(0), df.columns.get_level_values(1))]
            print('Columns are: ', ', '.join(df.columns))
            return df

        def __exit__(self, *a, **kw):
            return