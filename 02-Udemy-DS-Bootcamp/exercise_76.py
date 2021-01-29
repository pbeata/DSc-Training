
# Paul A. Beata
# January 28, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Task 0
# You are given a dataset with a single column of data:
data = pd.read_csv('./data/data_L76.csv')
data['count'] = 1
num_values = data['count'].count()
print(data)


# Task 1
# We want to divide the data using 6 intervals: 
# 	--> calculate the interval width by rounding up to a whole number
min_val = data['values'].min()
max_val = data['values'].max()
print("\ncheck the min/max values of our single column of data: ")
print([min_val, max_val])

# how many intervals do we want? 
num_intervals = 6
interval_width = (max_val - min_val) / num_intervals
rounded_width = int(np.round(interval_width, 0))
print("\nthe rounded interval width is = " + str(rounded_width))


# Task 2
# Create a frequency distribution table that shows:
# 	1. the intervals using the ROUNDED up value
#	2. the absolute frequency for each interval
#	3. the relative frequency for each interval

# define the column labels for our new data frame
column_headers = ['Interval', 'Start', 'End', 'Abs_Freq', 'Rel_Freq']

# define the intervals by looping over all intervals
intervals = np.ones((num_intervals + 1,), dtype=int)
intervals[0] = min_val
for i in range(1, num_intervals + 1):
	# new interval limit:
	intervals[i] = intervals[i-1] + rounded_width
	
	# current interval boundaries
	a = intervals[i-1]
	b = intervals[i]

	# Absolute Frequency:
	# count values that fall into this current interval range
	if (i == 1):
		n = data.loc[(data['values'] >= a) & (data['values'] <= b)].count()[0]
	else:
		n = data.loc[(data['values'] > a) & (data['values'] <= b)].count()[0]
	
	# Relative Frequency:
	# now determine the relative frequency for each interval
	r = n / float(num_values)

	# store current interval data as a row
	row = [i, a, b, n, r]

	# store that data row in our new data frame
	if (i == 1):
		df = pd.DataFrame([row], columns=column_headers)
	else:
		dfi = pd.DataFrame([row], columns=column_headers)
		df = df.append(dfi, ignore_index=True)

# print the final data frame table view
print('==========================================================')
print(df)
print('\n')


# Task 3
# Repeated Tasks 1-2 but do not round the interval up to an integer:

# (***Note: usually the exact width is more typical than rounding***)
print("the original interval width was = " + str(interval_width))

# define the intervals by looping over all intervals
intervals_real = np.ones((num_intervals + 1,), dtype=float)
intervals_real[0] = float(min_val)
for i in range(1, num_intervals + 1):
	# new interval limit:
	intervals_real[i] = intervals_real[i-1] + float(interval_width)
	
	# current interval boundaries
	a = intervals_real[i-1]
	b = intervals_real[i]

	# Absolute Frequency:
	# count values that fall into this current interval range
	if (i == 1):
		n = data.loc[(data['values'] >= a) & (data['values'] <= b)].count()[0]
	else:
		n = data.loc[(data['values'] > a) & (data['values'] <= b)].count()[0]
	
	# Relative Frequency:
	# now determine the relative frequency for each interval
	r = n / float(num_values)

	# store current interval data as a row
	row = [i, a, b, n, r]

	# store that data row in our new data frame
	if (i == 1):
		df2 = pd.DataFrame([row], columns=column_headers)
	else:
		dfi = pd.DataFrame([row], columns=column_headers)
		df2 = df2.append(dfi, ignore_index=True)	

# print the final data frame table view
print('==========================================================')
print(df2)
print('\n')


# Task 4
# Bonus: use matplotlib to automatically generate the histogram for this data
hist_bins = plt.hist(data['values'], bins=num_intervals)
plt.show()
