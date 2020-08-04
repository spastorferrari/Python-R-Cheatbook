def sum_even_values(*allVals):
    return sum(num for num in allVals if num%2==0)

sum_even_values(1,2,4,2,7,3,47,8,2,3)

10.2 % 1

10 %1


def sum_floats(*args):
    return sum(num for num in args if type(num) == float)

sum_floats(1,2,4,5,6)
