# import dependencies \\
import os
import argparse as ap
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_13\\recitation')

def read_file(filename=None) :
    if type(filename) != None:
        file = open(filename, 'r')
    a = file.readlines()
    return a

def count_vowels(filename = None) :
    string = read_file(filename)

    a = ''

    for line in string:
        a = a + line
        a  = a.replace(' ', '')
        a = a.replace('\n', '')

    count = 0
    for letter in a :
        if letter in 'aeiou' :
            count += 1
    return count

count_vowels('file01.txt')
 
