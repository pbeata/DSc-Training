
# Paul A. Beata
# January 28, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function to generate a frequency distribution table 
# input: data (DataFrame), num_intervals (int), col_name (str) 
# output: NEW df (DataFrame)
def create_freq_dist_table(data, num_intervals, col_name):
	
	# count the number of elements in the data set (rows)
	data['count'] = 1
	num_values = data['count'].count()

	# get the min and max values
	min_val = data[col_name].min()
	max_val = data[col_name].max()
	print("\ncheck the min/max/total values of our single column of data: ")
	print([min_val, max_val, num_values])

	# determine the interval width
	interval_width = (max_val - min_val) / num_intervals
	print("\nWith " + str(num_intervals) + " intervals the resulting interval width is " + str(interval_width) + " per interval.\n")

	# define the column labels for our new data frame
	column_headers = ['Interval', 'Start', 'End', 'Abs_Freq', 'Rel_Freq']

	# define the intervals by looping over all intervals
	intervals = np.ones((num_intervals + 1,), dtype=float)
	intervals[0] = min_val
	for i in range(1, num_intervals + 1):
		
		# new interval limit:
		x = intervals[i-1] + interval_width
		x = np.round(x, 4)
		intervals[i] = x
		
		# current interval boundaries
		a = intervals[i-1]
		b = intervals[i]

		# Absolute Frequency:
		# count values that fall into this current interval range
		if (i == 1):
			n = data.loc[(data[col_name] >= a) & (data[col_name] <= b)].count()[0]
		else:
			n = data.loc[(data[col_name] > a) & (data[col_name] <= b)].count()[0]
		
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

	# check the sum of the absolute frequency column
	check_sum = df['Abs_Freq'].sum()
	if (check_sum != num_values):
		print("***Warning: the number of values does not match the sum of absolute frequencies: ")
		print("There should be " + str(num_values) + " total values, but only " + str(check_sum) + " values were counted." )

	# output: new data frame with freq dist table
	return df





# Task 0
# You are given a dataset with a single column of data:
data = pd.read_csv('./data/data_L78.csv')
print(data)


# Task 1
# Create a frequency distribution table with 10 intervals:

# input
num_intervals = 10
col_name = 'values'
fdt = create_freq_dist_table(data, num_intervals, col_name)
print(fdt)


# Task 2
# Create a histogram using 10 intervals:

# Option A: use built-in histogram tool

start_col = fdt['Start']
end_col = fdt['End']
n = len(end_col)

bin_center = (start_col + end_col) * 0.5
bin_edges = np.append(start_col, [end_col[n-1]])
# print(bin_edges)  

freq = [0, 1, 2, 3]

plt.figure()
plt.hist(data[col_name], bins=num_intervals, edgecolor='black', linewidth=1.0, color='#abcabc')

plt.yticks(freq)
plt.xticks(bin_edges)

plt.xlabel('Given Data Values')
plt.ylabel('Absolute Frequency')

plt.show()

