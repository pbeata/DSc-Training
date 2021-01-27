
# Introduction to Python: Pandas and Data Filtering

import pandas as pd

# read in our data from the .csv file
# (it will be contained in the data frame named "data")
data = pd.read_csv('./out/pokemon_data_mod.csv')

# we can check the first few rows to make sure it loaded properly
print(data.head(5))

# filter such that only the Grass Pokemon are listed
grass_pokemon = data.loc[data['Type 1'] == 'Grass']

# to drop the initial index column and also "re-index" the new data
grass_pokemon = grass_pokemon.reset_index(drop=True, inplace=True)
print(grass_pokemon)
# print(grass_pokemon.describe())

# filter by two categories (two conditions)
print( data.loc[ (data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') ] ) 
print( data.loc[ (data['Type 1'] == 'Grass') | (data['Type 2'] == 'Poison') ] ) 
print( data.loc[ (data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') & (data['HP'] > 70) ] ) 

# show the data only where the names contain the string Mega:
print( data.loc[ data['Name'].str.contains('Mega') ] ) 

# ... now do the opposite: do not show any row whose name contains Mega:
print( data.loc[ ~data['Name'].str.contains('Mega') ] ) 

# working with regex:
fire_or_grass = data.loc[ data['Type 1'].str.contains('Fire|Grass', regex=True) ]
fire_or_grass = fire_or_grass.reset_index()
print( fire_or_grass.sort_values(['Type 1'], ascending=False) )
fire_or_grass.to_csv('./out/fire_or_grass_pokemon.csv', index=False)


# READ THE DOCUMENTATION ON REGEX BECAUSE THIS IS NOT WORKING FOR ME!

# data.loc[ data['Type 1'].str.contains('fire|grass', flags=re.IGNORECASE, regex=True) ]

# data.loc[ data['Name'].str.contains('^pi[a-z]*', flags=re.IGNORECASE, regex=True) ]



# Conditional Changes

# rename the Fire type Pokemon to "Flame" type (give them a new name)
data.loc[ data['Type 1'] == 'Fire', 'Type 1' ] = 'Flame'
print(data)

# now make all Flame Pokemon legendary
data.loc[ data['Type 1'] == 'Flame', 'Legendary' ] = True

# re-load the original data frame:
data = pd.read_csv('./out/pokemon_data_mod.csv')

# this will change the Generation and Legendary values to TEST_VALUE for 
# all Pokemon who have a Total value > 500 points:
# data.loc[data['Total'] > 500, ['Generation', 'Legendary'] ] = 'TEST_VALUE'
# print(data)


# Aggregate Statistics and the Groupby Function

# this is very useful to see aggregate stats by group
print(data.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

# doesn't really make sense in this context but you can do it
# print(data.groupby(['Type 1']).sum().sort_values('Defense', ascending=False)) 

print(data.groupby(['Type 1']).count().sort_values('Defense', ascending=False))

# if you want to do a clean count, you can add a column of just ones:
data['Count'] = 1
print(data.head(10))

# VERY USEFUL TO SEE THE COUNT OF EACH GROUP:
print(data.groupby(['Type 1']).count()['Count'])
print(data.groupby(['Type 1', 'Type 2']).count()['Count'])



# Working with Large Data Sets

# read in data by certain number of rows at a time

# NOT THIS ONE:
 # data_chunks = pd.read_csv('./old/pokemon_data_mod.csv', chunksize=5)

# THIS ONE IS A GOOD EXAMPLE:
# for df in pd.read_csv('./out/pokemon_data_mod.csv', chunksize=5):
	# print(df)

new_data = pd.DataFrame(columns=data.columns)
for df in pd.read_csv('./out/pokemon_data_mod.csv', chunksize=5):
	# print(df)
	results = df.groupby(['Type 1']).count()
	new_data = pd.concat([new_data, results])

