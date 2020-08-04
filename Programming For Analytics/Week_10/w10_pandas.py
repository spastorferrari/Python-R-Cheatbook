import os
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_10')

import pandas as pd
mydf = pd.read_csv('Employee data.csv', encoding= 'utf8')
mydf.head() # allows you to see structure of mydf


mydf.columns # lets you see all columns
mydf.dtypes # summarizes datatypes
mydf.iloc[5] # gets you entire row 5, every col included
mydf.isnull() # gets you all nulls

mydf.query('jobtime > 90')

groupedobj = mydf.groupby('minority') # groups by minority 0:1


# EXCERCISE 1: find the average salary

# use regex to replace salaries to a floating point number
mydf['salary'] = (mydf.salary.replace('[\$,)]', '', regex = True).replace('[(]', '-', regex = True).astype(float))

mydf.salary.mean() # 34419.56751054852


# EXCERCISE 2: handling the date columns
mydf.dtypes # we see that date is an object
import numpy as np
from dateutil.parser import parse

newdate = []
for x in mydf['bdate'] :
    try:
        newdate.append(parse(x))
    except:
        newdate.append(np.NaN)

mydf['bdate'] = newdate

list(mydf.bdate)
len(mydf)


a = ['tom', 'krish', 'nick', 'juli']
b = [25, 30, 26, 22]

c = list(zip(a,b))
