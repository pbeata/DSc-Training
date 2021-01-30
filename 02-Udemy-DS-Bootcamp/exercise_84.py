
# Paul A. Beata
# January 29, 2021

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew


def compute_skewness(x):
	n = len(x)
	x_mean = x.mean()
	
	a = x - x_mean
	b = a ** 3
	numer = (1 / n) * b.sum()
	
	c = a ** 2
	d = (1 / n) * c.sum()
	denom = (math.sqrt(d)) ** 3

	x_skew = numer / denom

	return x_skew


# Task 0
# load in our data set which has two columns labeled 'A' and 'B'
data = pd.read_csv('./data/data_L84.csv')
print(data.describe())


# Task 1
# compute skewness for data set A

print("\nCompute SKEWNESS using custom code for data column A: ")
a_skew = compute_skewness(data['A'])
print(a_skew)

print("\nCheck skewness result using scipy function skew() on data column A: ")
print(skew(data['A']))


# Task 2
# compute skewness for data set B

print("\nCompute SKEWNESS using custom code for data column B: ")
b_skew = compute_skewness(data['B'])
print(b_skew)

print("\nCheck skewness result using scipy function skew() on data column B: ")
print(skew(data['B']))


