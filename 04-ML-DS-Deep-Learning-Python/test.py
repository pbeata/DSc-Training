
# import our Python modules
import numpy as np
import matplotlib.pyplot as plt


# specify the mean as $27,000
# standard deviation = $15,000
# and we want 10,000 samples
incomes = np.random.normal(27000, 15000, 10000)
print(np.mean(incomes))

# make a histogram of the income data
plt.hist(incomes, 50)
# plt.show()

# what is the median salary?
print(np.median(incomes))

# now let's add in Jeff Bezos for fun!
incomes = np.append(incomes, [1000000000])
print(np.mean(incomes))
print(np.median(incomes))
