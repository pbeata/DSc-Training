
# Paul A. Beata
# February 01, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Exercise 99
# We are give a dataset that is approximately 
# normally distributed.

df = pd.read_csv('./data/data_L99.csv')
print(df)

# Task 1
# Calculate the mean and standard deviation
x_mean = df['weight'].mean()
x_stdev = df['weight'].std()
print([x_mean, x_stdev])

# Task 2
# Standardize the dataset 
df['weight_standardized'] = (df['weight'] - x_mean) / x_stdev
z_mean = df['weight_standardized'].mean()
z_stdev = df['weight_standardized'].std()
print([z_mean, z_stdev])

print(df)

# Task 
# Plot the data to see the change

plt.figure()
plt.hist(df['weight'], bins=20)

plt.figure()
plt.hist(df['weight_standardized'], bins=20)

plt.show()
