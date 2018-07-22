# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:18:46 2018

@author: Dipjyoti Metia
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#Read Dataset from csv file
melbourne_file_path = 'Melbourne_housing_DataSet/Melbourne_housing_FULL.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.head()
melbourne_data.describe()

reg= LinearRegression()

labels = melbourne_data['Price']
conv_dates = [1 if values == 2014 else 0 for values in melbourne_data['Date']]
melbourne_data['Date'] = conv_dates
train1 = melbourne_data.drop(['Id','Price'],axis=1)

print("Total Data",melbourne_data.size)
print("Total Train Data",train1.size)


x_train , x_test , y_train , y_test = train_test_split(train1 , labels , test_size = 0.10,random_state =2)

reg.fit(x_train,y_train)
