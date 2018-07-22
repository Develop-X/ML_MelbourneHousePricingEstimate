# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:06:04 2018

@author: Dipjyoti Metia
"""

#Data normalisation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os,sys
from scipy import stats
import numpy as np


#Read Dataset from csv file
melbourne_file_path = 'Melbourne_housing_DataSet/Melbourne_housing_FULL.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

for index, line in enumerate(open(melbourne_file_path, 'r').readlines()):
    w = line.split(' ')
    l1 = w[1:8]
    l2 = w[8:15]

    try:
        list1 = map(float, l1)
        list2 = map(float, l2)
    except ValueError:
        print('Line {i} is corrupt!'.format(i = index))
        break

    result = stats.ttest_ind(list1, list2)
    print(result[1])