# Intro to Data Visualization

# First we load the necessary libraries for our project
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


## 1. Basic Graphs

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
plt.savefig('fig1.svg', dpi=300)

# plot the figure to your screen
plt.show()



## 2. Bar Chart 
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


## Real World Examples

# NumPy + Pandas to work with csv type data


