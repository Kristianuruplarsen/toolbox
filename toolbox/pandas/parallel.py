
''' Tools for working with pandas dataframes in parallel
'''


import pandas as pd 
import numpy as np
from multiprocessing import Pool


def parallelize_rowwise(df, func, cores = 4, partitions = 10):
    """ Run a rowwise function in parallel across 
    multiple cores, each core handles 1 or more 
    partitions of the dataset. 

    Parameters
    ----------
    df (pd.DataFrame): dataframe to operate on.
    func (object): function to apply rowwise.
    cores (int): number of cores to use.
    partitions (int): number of partitions to split the 
                    dataset into.
    
    Returns
    -------
    pd.DataFrame
    """
    df_split = np.array_split(df, partitions)
    pool = Pool(cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df