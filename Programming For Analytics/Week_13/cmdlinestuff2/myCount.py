# \\ import dependencies
import argparse as ap

"""
Write a Python program that will do the following:

1. Compute the factorial of a given number.

2. Require the number to be provided as an argument for the program,
the factorial functionality is in a function.

3. Must have a help text associated.
"""

def myFactorial(n=0):
    """
    myFactorial takes a single argument: n=your_number.
    The program will return the factorial of your_number.
    If no n is specified, myFactorial will return 0.
    """

    if n <= 1:
        return 0
    else:
        prod = 1
        for i in range(1,n+1):
            prod *= i
        return prod

def tommy():
    myP = ap.ArgumentParser() # empty object

    myGroup = myP.add_mutually_exclusive_group() # creates group for myP

    # if the user specifies -d, they want a detailed output
    myGroup.add_argument('-d', '--detailed', action='store_true')
    # if the user specifies -s, they want a short output
    myGroup.add_argument('-s', '--short', action='store_true')
    # add an argument to the empty object
    myP.add_argument('myNum', help ='The number for which the factorial will be calculated.', type=int)
    # add another argument to the object
    myP.add_argument('-o', '--output', help='Send the result to a file.', action='store_true')

    myArgs = myP.parse_args() # parses through arguments in command prompt

    myResult = myFactorial(myArgs.myNum) # looks for myNum in args defined on cmd

    if myArgs.detailed:
        s = "The factorial for {:d} is {:d}".format(myArgs.myNum, myResult)
    elif myArgs.short:
        s = myResult
    else:
        s = "Factorial({:d}) = {:d}".format(myArgs.myNum, myResult)
    print(s)

    if myArgs.output:
        with open(myArgs.output, 'w') as f:
            f.write(s +'\n')

if __name__ == '__main__':
    main()
