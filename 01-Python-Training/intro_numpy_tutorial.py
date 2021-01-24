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


