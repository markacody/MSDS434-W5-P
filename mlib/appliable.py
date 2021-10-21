"""Appliable Functions to a Pandas GroupBy Operation (I.E Plugins)"""

import numpy as np


def tanimoto(x1, x2):
    """
    Tanimoto is a metric of the similarity of two sets. It is a ratio of the intersection over the union. Inputs are two lists [] or sets {}. Function converts to set if necessary and returns intersection / union. 
    """
    if type(x1) != set & type(x2) != set:
        x1 = set(x1)
        x2 = set(x2)
    return np.intersect1d(x1, x2, assume_unique=True)/np.union1d(x1, x2)


def npsum(x):
    """
    Input is one column or array. Output is numpy sum. 
    """
    return np.sum(x)


def npmedian(x):
    """
    Input is one column or array. Output is numpy median.
    """
    return np.median(x)
