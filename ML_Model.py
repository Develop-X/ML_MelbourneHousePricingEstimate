# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:06:49 2018

@author: dipjyoti.metia
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read Dataset from csv file
melbourne_file_path = 'Melbourne_housing_DataSet/Melbourne_housing_FULL.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.head()

melbourne_data.describe()
melbourne_data['Rooms'].value_counts().plot(kind='bar')
plt.title('Number of BedRooms')
plt.xlabel('Rooms')
plt.ylabel('Count')
sns.despine


plt.figure(figsize=(10,10))
sns.jointplot(x=melbourne_data['Lattitude'].values, y=melbourne_data['Longtitude'].values, size=10)
plt.ylabel('Longitude', fontsize=12)
plt.xlabel('Latitude', fontsize=12)
plt.show()
sns.despine

plt.scatter(melbourne_data['Price'],melbourne_data['Landsize'])


