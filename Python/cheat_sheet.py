
# Python Cheat Sheet
# Updated: April 15, 2021

# COMMON PACKAGES USED
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%config Completer.use_jedi = False

# TRAIN-TEST SPLIT TEMPLATE
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=101)
