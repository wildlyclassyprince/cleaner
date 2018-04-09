# -*- coding: utf-8 -*-

# The suspects ...
import pytest
import warnings

import numpy as np
import pandas as pd

values = pd.DataFrame({'Vehicle' : ['BMW', 'Benz', 'Audi', 'Toyota'],
                       'Price' : [15000, 18000, 16000, 10500]})

def test_dataframe(data):
    global values
    assert (type(values) == type(data))

def test_unique_value_counts():
    pass

def test_word_case():
    pass

def test_drop_fields():
    pass

def test_remove_columns():
    pass
