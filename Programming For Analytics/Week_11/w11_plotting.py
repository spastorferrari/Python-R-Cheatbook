import os
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_11')

import pandas as pd
df = pd.read_csv('tips.csv')
df

# 1. find and plot the proportion of parties by size for each day. For instance if  10 parties had food on Friday and three were party of 2, five were party of 4 and 3 were party of 5. Then the proportions for size of party of 1, 2, 3, 4, 5, 6 and 7 would be 0.00, 0.20, 0.00, 0.50, 0.30, 0.00, and 0.00 respectively.


partycounts = pd.crosstab(df['day'],df['size']) # makes df with (row,column)
sumbyday = partycounts.sum(1) # we sum by row 1 [day]
sumbyday
pprops = partycounts.div(sumbyday, axis=0)
pprops

pd.crosstab(df['day'], df['size'], normalize='index') # condensed in one line.

import matplotlib.pyplot as plt
pprops.plot(kind = 'bar')
pprops.plot()

# Draw a histogram for tips
df['tip'].hist() # plots series
df[['tip']].hist() # plots histogram

# make a barplot or column graph of the average tip paid and average party size
df[['tip','size']].mean().plot.bar(color=['lightsalmon','lightseagreen'])

# plot the average total bill by day
df.groupby('day')['total_bill'].mean().plot(kind='bar', color=['lightsalmon', 'lightseagreen', 'palevioletred', 'peru'])

# Sebastián Pastor Ferrari © - 2019
