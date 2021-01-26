'''
Introduction to NumPy in Data Science
by Real Python (https://realpython.com/numpy-tutorial/)

DATE:  Januray 23, 2021

Core Concepts:
1. creating arrays 
2. treating complete arrays like individual values to do  
vectorized calculations
3. using NumPy functions to modify and aggregate your data

'''

import numpy as np
import matplotlib.pyplot as plt

print("\nIntroduction to NumPy for Data Science")

# Intro Example: Curving the grades on a test

# We are going to do the following:
#   1. Make the average score a C 
# 	2. Make sure no one's score is hurt
#	3. Make sure no one gets over a 100

def curve(grades, curve_center):
	avg_grade = grades.mean()
	change = curve_center - avg_grade
	new_grades = grades + change		# vectorization and broadcasting
	return np.clip(new_grades, grades, 100)  
	# clip function to make sure no grade is > 100% or less than the the old array
	# usage: numpy.clip(a, a_min, a_max, out=None, **kwargs)


# define the "grades" and the "CENTER" of the curve
CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])   # creates a 1D array (int64)
print("\nThe original list of grades: ")
print(grades)

# check the average using the NumPy mean() function
orig_avg = grades.mean()
print("The original average grade in the class was " + str(orig_avg) + "%.")

# apply the curve to the grades
curved_grades = curve(grades, CENTER)
print("\nThe new list of curved grades: ")
print(curved_grades)

# check the new average of the curved grades
curved_avg = curved_grades.mean()
print("The new \"curved\" average grade in the class was " + str(curved_avg) + "%.")
print(" ")

# ===============================================

# Array Shapes and Axes

# shape

# The shape function returns a tuple of the size 
# of the array in each dimension.

temperatures = np.array([
	29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
	12.6, 49.9, 38.6, 31.3,  9.2, 22.2
	]).reshape(2,2,3)

print(temperatures.shape)
print(temperatures)

print(np.swapaxes(temperatures, 1, 2))


# understanding axes

# It is important to know which data is in which axis.
# For example, for some functions, specifying the axis 
# will change the expected output.

table = np.array([
	[5, 3, 7, 1],
	[2, 6, 7, 9],
	[1, 1, 1, 1],
	[4, 3, 2, 0]
	])

print(table.max())			# returns largest value in the entire array (default max)
print(table.max(axis=0))	# returns the max value for each "column"
print(table.max(axis=1))	# returns the max value for each "row"

# broadcasting

# *** arrays can be broadcasted against each other if their dimensions match 
# or if one of the arrays has a size of 1

A = np.arange(32).reshape(4, 1, 8)  
B = np.arange(48).reshape(1, 6, 8)

# axis 0: value in "1" spot of B will be broadcasted to the "4" elements of A
# axis 1: value in "1" spot of A will be broadcasted to the "6" elements of B
# axis 2: this axis has matching dimensions of "8" in both A and B

# print(A)
# print(B)
print(A+B)

# ===============================================

# Data Science Operations: Filter, Order, Aggregate

# Indexing

# Example: confirming the Dürer square

square = np.array([
	[16, 3, 2, 13],
	[5, 10, 11, 8],
	[9, 6, 7, 12],
	[4, 15, 14, 1]
	])

for i in range(4):
	assert square[:, i].sum() == 34
	assert square[i, :].sum() == 34

assert square[1:3,1:3].sum() == 34

assert square[:2,:2].sum() == 34
assert square[:2,2:].sum() == 34

assert square[2:,:2].sum() == 34
assert square[2:,2:].sum() == 34

# test the sum() function on the whole array and use axes
print(square.sum())
print(square.sum(axis=0))
print(square.sum(axis=1))

# Masking and Filtering

# Index-based selection is great for when you need consecutive values of an array.
# But if you want to filter your data based on more complicated nonuniform
# or nonsequential criteria, then you need the concept of a "mask".

# A mask has the same shape as your data, but it contains Boolean values.

# Example 1:
x = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
print(x)

mask = x % 4 == 0
print(mask)

print(x[mask])

# or
y2 = x[x % 2 == 0]
y4 = x[x % 4 == 0]
print(y2)
print(y4)

# Example 2:
# The normal distribution has ~95% of its values occur 
# within 2 standard deviations of the mean.

# use random module from NumPy to generate random #s
from numpy.random import default_rng

# this is the default generator object
rng = default_rng()
vals = rng.standard_normal(10000)
print(vals[:5]) 

# alternative: 
rng = np.random.default_rng()
z = rng.random((10000,))
print(z[:5])

# compute standard deviation
stdev = vals.std()

# use filter to return only the values within 2 stdev's of the mean:
filtered = vals[(vals > -2 * stdev) & (vals < 2 * stdev)]
# ** notice we use the & symbol to do a vectorized operation

# compute fraction of values in the filtered range:
m1 = filtered.size
m2 = vals.size
check_percent = (m1 / m2) * 100
print(str(check_percent) + "%")

# Array Transpose

aa = np.array([[1, 2],
			  [3, 4],
			  [5, 6]])
print(aa)
print(aa.T)

# [ or use aa.transpose() ]

# Sorting Arrays

data = np.array([
	[7, 1, 4],
	[8, 6, 5],
	[1, 3, 2]
	])

# sorts each row
print("Sort 1:")
print(np.sort(data))

# flattens the array and sorts the data as if 1D
print("Sort 2:")
print(np.sort(data, axis=None))

# sorts each column
print("Sort 3:")
print(np.sort(data, axis=0))

# sorts each row
print("Sort 4:")
print(np.sort(data, axis=1))

# Concatenate Arrays

# ** NOTE: this functions take in a tuple as input!

A = np.array([
		[4, 8],
		[6, 1]
	])

B = np.array([
		[3, 5],
		[7, 2]
	])

# horizontal stack:
print(np.hstack((A, B)))  
# [ A B ]

# vertical stack
print(np.vstack((B, A)))  
# | B |
# | A |

# concatenate
print(np.concatenate((A, B)))
print(np.concatenate((A, B), axis=None)) # flattens the arrays and concatenates them


# Aggregation

# generate a random array of data
rng = np.random.default_rng()
N = 10000
x = rng.random((N,))
print(x[:5])

print("sum(x) = " + str(x.sum()))
print("max(x) = " + str(x.max()))
print("min(x) = " + str(x.min()))
print("mean(x) = " + str(x.mean()))
print("std(x) = " + str(x.std()))

# plot the random data
x = np.arange(N)
y = np.sort(x)
# plt.plot(x, y, 'k.')
# plt.show()

# d = np.random.laplace(loc=15, scale=3, size=500)

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=y, bins='auto', color='#0504aa') #, alpha=0.7, rwidth=0.85)

# plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My First Histogram')

# plt.text(23, 45, r'$\mu=15, b=3$')
# maxfreq = n.max()
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

# Example: Normal Distribution
mu = 0
sigma = 0.1
s = np.random.normal(mu, sigma, N)
print("check mean: " + str(s.mean()))
print("check std:  " + str(s.std()) )
count, bins, ignored = plt.hist(s, 30, density=True)
plt.show()
