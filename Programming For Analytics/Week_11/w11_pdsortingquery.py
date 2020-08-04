import os
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_11')

import pandas as pd

# reading csv files is a lot easier with pandas
# the parameter index_col = 0, makes the first column equal the index
df = pd.read_csv('21-Data management with Pandas.csv', index_col=0)
df.head(6) # first six results

# 1. extract the index, columns, and values
index = df.index
columns = df.columns
values = df.values
df.index
df.columns


# 2. explore datatypes (use type())
type(index) # pandas.core.indexes.base.Index
type(columns) # pandas.core.indexes.base.Index
type(values) # numpy.ndarray


# 3. Indexing: selecting a single column
t2 = df['Test2']
type(t2) # pandas.core.series.Series

# 3.1 Selecting multiple columns with just the indexing operator
tests = df[['Test1', 'Test2', 'Test3']]
type(tests) # pandas.core.frame.DataFrame

## NOTES on 3: t2 is a series extracted from df, while tests is a subdf extracted from df. [] = SERIES & [[]] = DATAFRAME
t2df = df[['Test2']]
type(t2df) # pandas.core.frame.DataFrame


# 4. Location operator (.loc): helps us subset rows and columns
gitaSeries = df.loc['Gita'] # allows you to access all information concerning 'Gita'
gitaDf = df.loc[['Gita']]

bellatommmy = df.loc[['Bella', 'Tommy']]
df.loc[[df.index[13], df.index[0]]] # same thing as above


# 5. Indexing: find all rows up to Ali, in steps of 2
uptoAli = df[:'Ali':2]

# Slice from Sam to Bella
df.loc['Sam':'Bella']


# 6. Selecting rows and comuns simultaneously
# find Test1 and Test3 for Mary and Jolly only

df.loc[['Mary', 'Jolly'],['Test1', 'Test3']]

# get all columns for Mary and Jolly
df.loc[['Mary', 'Jolly']]

# get Test1 and Test3 for all rows
df.loc[:,['Test1', 'Test3']]
df.loc[:'Ali':2, ['Sex', 'Test3']] # upto Ali in 2 steps, columns Sex and Test3.


# 7. using .iloc : allows us to subset by index number
df.iloc[[2]]

# select rows from 2-5
df.iloc[1:5]
# select from 4 till end
df.iloc[3:]

# select rows 4 and 7, and columns 1 and 3
df.iloc[[4,7],[1,3]]

# select rows 2-7, and columns 1-4
df.iloc[2:7, 1:4]

# select row 3 and column 4
df.iloc[[3],[4]] # Polly >> Test 4

# return the VALUE of row 3 column 4
df.iloc[3,4] # returns 4


# 8. Query function
df[df['Section'] == 'A'] # every row for which Section is A

df.query('Section == "A"')

# Select all females in section A
df.query('Section == "A" & Sex == "F" ')

# all males and only columns Sex and Test3
df.query('Sex == "M"').loc[:,['Sex','Test3']]

# all students who have been showing worsening performance over time
df.query('Test1>Test2>Test3')
df.query('Test1 == Test2 or Test2 == Test3')

target_score = 8
df.query('Test2 == @target_score') # you use @ to call a variable within quotes


# 9. sorting dataframes
df.sort_index()
df.sort_index(ascending = False)

df.sort_values('Test1', ascending = False)

df.sort_values(['Test1', 'Test3'], ascending=[False,True])
