
# Paul A. Beata
# January 28, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./data/income_data.csv')
print(data)

x = data['Income']

x_sum = 0.0
for xi in x:
	x_sum += xi

n = len(x)
x_mean = x_sum / n
print([x_mean, x.mean()])


