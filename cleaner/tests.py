#-*- coding: utf-8 -*-

'''
This script contains tests for `cleaner.py`.
'''

__author__ = "wildlyclassyprince"
__license__ = "GNU"
__version__ = "0.1.0"
__maintainer__ = "wildlyclassyprince"
__email__ = "lihtumb@gmail.com"
__status__ = "Initial Tests"

# The suspects
import pandas as pd
import numpy as np

# Test size of dataframe
def test_size_of_dataframe_rows():
    '''
    Tests the size of the dataframe.
    Dataframe should not be empty.
    '''
    assert df.shape[1] > 0
    
def test_size_of_dataframe_columns():
    '''
    Tests the size of the dataframe.
    Dataframe should have more that one column.
    '''
    assert df.shape[0] > 1
