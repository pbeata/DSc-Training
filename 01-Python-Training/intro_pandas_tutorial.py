

# Why Pandas?
#  - flexibility of Python to do lots of cool things with your data
#  - allows you to work with big data


# import the pandas module
import pandas as pd

# load the CSV data into a "data frame" object
data = pd.read_csv('./data/pokemon_data.csv')

# ... we can also do the same thing with "tab-separated" TXT data 
# as well as EXCEL data (but only if it is in the form of .xls)
data_text = pd.read_csv('./data/pokemon_data.txt', delimiter='\t')
# data_excel = pd.read_excel('./data/pokemon_data.xlsx')

# check the first or last few rows to see the structure of the data
print(data.head(10))
print(data.tail(3))

# we can do the same with the data read from other sources as well
print(data_text.head(3))
# print(data_excel.head(3))

# Reading Data in Pandas

# read the headers
print(data.columns)

# read a single column
print(data['Name'])
print(data['Name'][0:5])

# read multiple columns
print(data[['Name', 'Type 1', 'HP']])

# read each row
print(data.iloc[0:4])

# read a specific cell location
print(data.iloc[2,1])

# for index, row in data.iterrows():
# 	print(index, row['Name'])

# filtering
fire_pokemon = data.loc[data['Type 1'] == "Fire"]
print(fire_pokemon)

# print a summary of the data (aggregate stats)
print(data.describe())

# describe gives high-level stats view
print(fire_pokemon.describe())

# sorting 
print(data.sort_values(['Name'], ascending=False))

# sorting with two columns 
print(data.sort_values(['Type 1', 'HP'], ascending=[True, False]))

# Making changes to the data

# add all the stats columns individually to make an OVERALL column
data['Total'] = data['HP'] + data['Attack'] + data['Defense'] + data['Sp. Atk'] + data['Sp. Def'] + data['Speed']
print(data['Total'])


