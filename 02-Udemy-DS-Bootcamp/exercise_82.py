
# Paul A. Beata
# January 28-29, 2021

# Exercise 84: mean, median, and mode

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# compute the mean, mode, and median

data = pd.read_csv('./data/income_data.csv')

print('\nOriginal income data set: ')
print(data)

x = data['USA']

# find the mean manually:

x_sum = 0.0
for xi in x:
	x_sum += xi

n = len(x)
x_mean = x_sum / n

# find the median manually:

y = data['USA'].sort_values(ignore_index=True)

print('\nSorted income data set: ')
print(y)

m = (n - 1) / 2
if ( (n - 1) % 2 == 0 ):
	x_med = y[m]
else:
	m1 = math.floor(m)
	m2 = math.ceil(m)
	x_med = (y[m1] + y[m2]) / 2.0

x_mode = data['USA'].mode()[0]

# ===================================================================

print("\nThe mean of this data set is: $%.2f " % x_mean)
# print([x_mean, x.mean()])

print("\nThe median of this data set is: $%.2f " % x_med)

print("\nThe mode of this data set is: $%.2f " % x_mode)

print("\n***Note: Usually, whenever we have research on income, we use the median income, instead of the mean income. Income is an example where averages are meaningless. You should be aware that the correct measure to use depends on the research that you are conducting.\n")

# ===================================================================

# Exercise 86: variance

def compute_pop_var(x):
	N = len(x)
	mean_pop = x.mean()
	x2 = (x - mean_pop) ** 2
	Pvar = x2.sum() / N
	return Pvar

def compute_sample_var(x):
	n = len(x)
	mean_sample = x.mean()
	x2 = (x - mean_sample) ** 2
	Svar = x2.sum() / (n - 1)
	return Svar


# Task 1
# Decide whether this is population or sample data:
# 	==>	In this case, with only 11 data points representing
# 		the salaries of 11 people in whole population
#		of the US, it is safe to assume that this is a SAMPLE
#		since we do not have data for the entire US population.

# Task 2	
# Compute the variance for the income data:

Svar = compute_sample_var(data['USA'])
print("the SAMPLE variance is computed as: \n  $%.2f" % Svar)

Pvar = compute_pop_var(data['USA'])
print("if we mistakenly assumed POPULATION data, the variance would be: \n  $%.2f" % Pvar)

# Task 3
# What does this variance value tell us? 
print("\n***Note: This value for the variance seems to indicate that the salary data we have obtained is very disperse (large spread with high variability). There seems to be great dispersion in the income of residents of the United States. ")

# ===================================================================

# Exercise 88: coefficient of variation 

# - Comparison of Income Data from Two Countries
# - Two data columns: USA and Denmark

usa = data['USA']
denmark = data['Denmark']

# Is this population or sample data?
# 	==>	We know this is SAMPLE data because we only have 11 
#		salaries from each country. 

# Calculate the coefficient of variation in multiple steps:
#	1. compute the mean
#	2. compute the variance
#	3. get the standard deviation using sqrt(var)
#	4. compute the coefficient of variation as cv = (stdev / mean)

# Compute the sample variance for each country:
usa_var = compute_sample_var(usa)
denmark_var = compute_sample_var(denmark)

# Compute the standard deviation
usa_stdev = math.sqrt(usa_var)
denmark_stdev = math.sqrt(denmark_var)

# Compute the coefficient of variation
usa_cv = usa_stdev / usa.mean()
denmark_cv = denmark_stdev / denmark.mean()

# Show output

print("\nThe sample mean income for the USA is %.2f USD." % usa.mean() )
print("The sample mean income for Denmark is %.2f EURO." % denmark.mean() )

print("\nThe sample standard deviation for income in the USA is %.2f USD." % usa_stdev )
print("The sample standard deviation for income in Denmark is %.2f EURO." % denmark_stdev )

print("\nThe coefficient of variation of income in the USA is %.3f" % usa_cv)
print("The coefficient of variation of income in Denmark is %.3f" % denmark_cv)


# =========================================================


# Exercises 90 and 92

def compute_sample_covariance(x, y):
	m = len(x)
	n = len(y)
	if (m != n):
		print("***Error: arrays must have the same size: %d and %d are different." % (m, n))
		Sxy = False
	else:
		xx = x - x.mean()
		yy = y - y.mean()
		z = np.multiply(xx, yy)
		Sxy = z.sum() / (n - 1)
	return Sxy


def compute_population_covariance(x, y):
	M = len(x)
	N = len(y)
	if (M != N):
		print("***Error: arrays must have the same size: %d and %d are different." % (M, N))
		Sxy = False
	else:
		xx = x - x.mean()
		yy = y - y.mean()
		z = np.multiply(xx, yy)
		Sxy = z.sum() / N
	return Sxy	


# Example:

writing = np.array([344, 383, 611, 713, 536])
reading = np.array([378, 349, 503, 719, 503])

Sxy_sample = compute_sample_covariance(writing, reading)
Sxy_population = compute_population_covariance(writing, reading)

print("\nthe sample covariance for SAT scores:	    " + str(Sxy_sample))
print("the population covariance for SAT scores:   " + str(Sxy_population))

# Correlation Coefficients

writing_var = compute_sample_var(writing)
writing_stdev = math.sqrt(writing_var)

reading_var = compute_sample_var(reading)
reading_stdev = math.sqrt(reading_var)

CC = Sxy_sample / (writing_stdev * reading_stdev)
print("\nthe correlation coefficient for SAT scores: %.3f " % (CC))

if (CC > 0.9):
	print("\nSince %.3f is very close to 1.0, we can say that there is a very strong positive correlation between the two datasets\n" % (CC))


