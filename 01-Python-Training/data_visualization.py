# Intro to Data Visualization
# with Keith Galli (YouTube)
# January 2021


# First we load the necessary libraries for our project
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


# Example 1
def run_basic_plot():
	# re-size your plot
	# plt.figure(figsize=(5,5))
	# can also include a dpi option when specifying the figsize

	# data set 1
	x = [0,1,2,3,4]
	y = [0,2,4,6,8]
	plt.plot(x, y, label='$y(x) = 2x$', color='red', linewidth=2, marker='o', markersize=8, linestyle='--')

	# data set 2
	x2 = np.arange(0, 4.5, 0.1)
	y2 = x2 ** 2
	n = len(x2)
	m = math.ceil(n/2)
	plt.plot(x2[:m], y2[:m], label='$y=x^2$', linestyle='-', color='blue', linewidth=2)
	plt.plot(x2[m:-1], y2[m:-1], label='$y=x^2$ (future)', linestyle=':', color='blue', linewidth=2)

	# define the chart title and label the x- and y-axes
	plt.title('Basic Scatter Plot', fontdict={'fontsize': 20})
	plt.xlabel('(x-axis label example)')
	plt.ylabel('(y-axis label example)')

	# customize your x- and y-ticks as well
	plt.xticks([0,1,2,3,3.5,4])
	plt.yticks([0,2,4,6,7,8])

	# display the legend (according to your "labels" defined in plt.plot)
	plt.legend()

	# save the figure
	plt.savefig('./out/fig1.png', dpi=300)
	plt.savefig('./out/fig1.svg', dpi=300)

	# plot the figure to your screen
	plt.show()


# Example 2
def run_bar_chart():
	bar_labels = ['A', 'B', 'C']
	bar_values = [1, 4, 2]

	plt.figure(figsize=(6,4))

	bars = plt.bar(bar_labels, bar_values)

	patterns = ['/', 'O', '*']
	for bar in bars:
		bar.set_hatch(patterns.pop(0))

	# bars[0].set_hatch('/')
	# bars[1].set_hatch('O')
	# bars[2].set_hatch('*')

	plt.title('Bar Chart Example')
	plt.show()


# Example 3
def run_gas_example():
	# load in our gas prices data first into its data frame
	gas_data = pd.read_csv('./data/gas_prices.csv')
	print(gas_data.head(5))

	# plt.figure(figsize=(8,5))

	# we are going to plot gas prices VS year for various countries
	plt.plot(gas_data.Year, gas_data.USA, 'b.-', label='United States')
	plt.plot(gas_data['Year'], gas_data['Canada'], 'r.-')
	plt.plot(gas_data['Year'], gas_data['South Korea'], 'g.-')
	plt.plot(gas_data['Year'], gas_data['Australia'], 'm.-')

	# or we can plot every country like this:
	# for country in gas_data:
	# 	if country != 'Year':
	# 		print(country)
	# 		plt.plot(gas_data.Year, gas_data[country], marker='.')

	# title and legend formatting
	plt.title('Gas Prices over Time in USD', fontdict={'fontweight': 'bold', 'fontsize': 18})
	plt.legend()

	# fix the xticks
	print(gas_data.Year[::3])
	# plt.xticks(gas_data.Year[::3])

	# we can also add in the single year of 2011 like this:
	plt.xticks(gas_data.Year[::3].tolist() + [2011])

	# format labels for the two axes
	plt.xlabel('Year')
	plt.ylabel('Price in USD')

	# finally, show the plot
	plt.savefig('./out/gas_prices_over_time.png', dpi=300)
	plt.savefig('./out/gas_prices_over_time.svg', dpi=300)
	plt.show()


# Example 4
def run_fifa_example():

	# load in the data from our FIFA spreadsheet 
	fifa = pd.read_csv('./data/fifa_data.csv')
	print(fifa.head(10))

	# print the column labels
	print(fifa.columns)

	# check the top 10 overall players (already sorted by Overall)
	print(fifa[['Name', 'Overall']].head(10))

	# check the aggregrate stats of the whole data set
	print(fifa.describe())

	# HISTOGRAMS
	# my_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	my_bins = [40, 50, 60, 70, 80, 90, 100]
	plt.hist(fifa['Overall'], bins=my_bins, color='#abcdef')
	plt.xticks(my_bins)

	plt.title('Distribution of Player Skill in FIFA \'18')
	plt.xlabel('Skill Level: Overall')
	plt.ylabel('Number of Players')
	# plt.show()

	# PIE CHARTS
	# compare the number of left-footed vs right-footed players in FIFA
	left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
	right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
	print(left)
	print(right)

	plt.figure(figsize=(4,3))
	
	my_labels = ['Left', 'Right']
	my_colors = ['orange', 'aqua']

	plt.title('Foot Preference of all FIFA Players')
	plt.pie([left, right], labels=my_labels, colors=my_colors, autopct='%.2f %%')
	# plt.show()

	# player weight
	# reset the weights to only use integers

	fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

	print(fifa.Weight.head(10))

	light = fifa.loc[fifa.Weight < 125].count()[0]
	light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
	medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
	medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
	heavy = fifa.loc[fifa.Weight > 200].count()[0]

	weight_groups = [light, light_medium, medium, medium_heavy, heavy]
	weight_labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
	print(weight_groups)

	plt.figure(figsize=(6,3))
	plt.style.use('ggplot')

	# how to make the pie chart look nicer?

	# set the percentage distance 

	# use the explode option to see the pie pieces better

	my_explode = (.4, .2, .0, .0, .4)
	plt.pie(weight_groups, labels=weight_labels, autopct='%.1f %%', pctdistance=0.8, explode=my_explode)

	plt.title('Weight Distribution of FIFA \'18 Players')

	# plt.show()



	# BOX AND WHISKERS PLOT
	barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
	madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
	revolution = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

	box_labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

	plt.style.use('default')
	plt.figure(figsize=(5,7))
	
	boxes = plt.boxplot([barcelona, madrid, revolution], labels=box_labels, patch_artist=True, medianprops={'linewidth': 2})
	for box in boxes['boxes']:
		
		# set box edge color
		box.set(color='#4286f4', linewidth=2)
		
		# set box fill color
		box.set(facecolor='#e0e0e0')


	plt.title('Professional Soccer Team Comparison')
	plt.ylabel('FIFA Overall Player Ratings')
	plt.show()




## Part A: Basic Graphs

# 1. Basic Plot with Two Curves
# run_basic_plot()

# 2. Simple Bar Chart 
# run_bar_chart()


## Part B: Real World Examples

# Now we will use NumPy + Pandas to work with csv type data

# 3. Gas Price Data
# run_gas_example()

# 4. FIFA Soccer Data
run_fifa_example()



