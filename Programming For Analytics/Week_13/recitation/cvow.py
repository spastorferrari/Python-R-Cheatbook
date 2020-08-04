# import dependencies \\
import os
import argparse as ap
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_13\\recitation')

def read_file(filename=None) :
    if type(filename) != None:
        file = open(filename, 'r')
    a = file.readlines()
    return a

def count_vowels(filename=None) :
    string = read_file(filename)

    a = ''

    for line in string:
        a = a + line
        a  = a.replace(' ', '')
        a = a.replace('\n', '')

    countV = 0
    countT = 0
    for letter in a :
        countT += 1
        if letter in 'aeiou' :
            countV += 1
    countV = '{0:,}'.format(countV)
    countT = '{0:,}'.format(countT)
    return (countV, countT)

def give_output() :
    myP = ap.ArgumentParser()
    myGroup = myP.add_mutually_exclusive_group()

    myGroup.add_argument('-d', '--detailed', action='store_true', help='Returns detailed output.')
    myGroup.add_argument('-s', '--short', action='store_true', help='Returns value-pair output.')
    myP.add_argument('fileName', help='The filename you want to parse.')

    myArgs = myP.parse_args()

    vowels = count_vowels(myArgs.fileName)[0]
    total = count_vowels(myArgs.fileName)[1]
    name = str(myArgs.fileName).strip('.txt')

    if myArgs.detailed:
        a = 'Out of {} characters in {}, {} are vowels.'.format(total, name, vowels )
    else:
        a = 'Vowels: {}'.format(count_vowels(myArgs.fileName)[0])
    print(a)

if __name__ == '__main__':
    give_output()

# © Sebastián Pastor Ferrari - 11.24.2019
