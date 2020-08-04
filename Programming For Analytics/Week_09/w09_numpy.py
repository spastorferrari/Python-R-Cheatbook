import numpy as np

# one dimensional array of numbers 1-8
myonedim = np.array(list(range(1,9)))

# two dimensional array of numbers 1-3 and numbers 4-6
# we need a ton of parenthesis since it needs  to be passed as tuple
mytwodim = np.array((list(range(1,4)), list(range(4,7))))

# three dimensional array
# a list with three lists, each containing three lists within them
mythreedim = np.array([[  [ 1,  2], [ 3,  4], [ 5,  6]], # first dim
                        [[ 7,  8], [ 9, 10], [11, 12]], # second dim
                        [[13, 14], [15, 16], [17, 18]]]) # third dim

# dimensions in an array (3)
mythreedim.ndim
# shape of array (3,3,2)
mythreedim.shape


# Creating an array from range() and reshaping it
x = np.array(range(24)) # array
x.shape # 24 rows and 1 column

y = x.reshape((3,4,2)) # reshapes to 3 groups of 4 rows and 2 columns


# Creating an arrange with np.reshape() allows us to range and reshape in one operation
a = np.reshape(np.arange(9),(3,3)) # numbers 0-8, in 3 rows and 3 cols
a # array([[0, 1, 2],
    #   [3, 4, 5],
    #  [6, 7, 8]])

# Slicing arrays
print(a[::]) # a[start:end:step]
print(a[:,0]) # returns column 0 [0,3,6]

# another example of np.reshape(np.arrange())
a = np.reshape(np.arange(16), (4,4)) # numbers 0-15, 4 rows and 4 cols
a # array([[ 0,  1,  2,  3],
    #   [ 4,  5,  6,  7],
    #   [ 8,  9, 10, 11],
    #   [12, 13, 14, 15]])


## EXCERCISE 1: Use the [:] operator to extract the three 2x2 diagonal slices from the array shown above

a[0:2] # first two
a[1:3] # second two
a[2:4] # third two

# EXCERCISE 2: Create a 4x3 array, obtain the sum of each row, obtain the sum of each column

a = np.reshape(np.arange(12), (4,3))
# array([[ 0,  1,  2],
    #   [ 3,  4,  5],
    #   [ 6,  7,  8],
    #   [ 9, 10, 11]])

# sum of cols. builtin sum()
print(sum(a))

# sum of rows. for row in a print sum(row)
for row in a:
    print(sum(row))
