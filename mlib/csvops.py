"""
CSV Operations Module (csvops):
Basic services using Pandas for csv files: list column names, aggregate columns, and group by operations. 
I/O Performance in Pandas:
    http://pandas.pydata.org/pandas-docs/stable/io.html#io-perf
"""

# Imports
from sensible.loginit import logger
import pandas as pd

log = logger(__name__)
log.debug('imported csvops module')


def ingest_csv(data):
    """
    Input is csv file. Output is pandas dataframe.
    """
    df = pd.read_csv(data)
    return df


def list_column_names(data):
    """
    Input is csv file. Column names are logged. Output is the list of column names. 
    """
    df = ingest_csv(data)
    colnames = list(df.columns.values)
    cols_msg = 'Column names: {colnames}'.format(colnames=colnames)
    log.info(cols_msg)
    return colnames


def aggregate_column_name(data, groupby_name, apply_name):
    """
    Input is csv file, the group by column name, and the apply name, that is, the column whose sum you want. Output is the result. 
    """
    df = ingest_csv(data)
    return df.groupby(groupby_name)[apply_name].sum()


def group_by_operations(data, groupby_name, apply_name, func=npsum):
    """
    Input is csv file, the group by column name, the apply column name, and the function you want applied. Output is the result. Allowable functions are from the appliable module.
    """
    df = ingest_csv(data)
    grouped = df.groupby(groupby_name)
    applied = grouped[apply_name].apply(func)
    return applied
