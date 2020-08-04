import os
import seaborn as sns
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_15')

# 1. Explore text1.txt and read in the contents as numbers into a list of numbers.

# example 1: using for loop
file = open('text1.txt', 'r')
numbers = []
for line in file.readlines():
    numbers.append(line.strip('\n'))

# example 2: using read().split()
file1 = open('text1.txt', 'r')
numbers1 = file1.read().split('\n')

# example 3: nested with statement
with open('text1.txt', 'r') as file2:
    numbers2 = file2.read().split('\n')

# convert the values of list to integers using list unpacking
mynumlist = [int(num) for num in numbers2]
# or float:
mynumlistFloat = [float(num) for num in numbers2]

# function any of the above!
def numsparser(filename, float_bool=True):
    with open(filename, 'r') as file:
        numbers = file.read().split('\n')
    if float_bool:
        return([float(num) for num in numbers])
    if not float_bool:
        return([int(num) for num in numbers])

numsparser('text1.txt')

# 2. Import iris dataset from seaborn
iris = sns.load_dataset('iris')
iris['species'].value_counts().plot('bar')

# histogram for petal width
iris['petal_width'].hist()

# scatter plot for sepal length and sepal width
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)

# boxplot on subsets
df2 = iris[['sepal_length', 'sepal_width']]
df2.boxplot()
# © Sebastián Pastor Ferrari - 12.03.2019
