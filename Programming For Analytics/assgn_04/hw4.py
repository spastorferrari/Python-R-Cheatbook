import os
import pandas as pd

os.chdir('/Users/Sebastian Pasotr/Documents/Data_Coding/Python Root/assgn_04')

file1 = open('script01.txt','r')
file2 = open('script02.txt', 'r')

listFile1 = list(file1.read().split())
listFile2 = list(file2.read().split())
listAll = listFile1 + listFile2
d1 = {}
listAll

for entry in listAll:
    for letter in entry:
        if letter.lower() in d1:
            d1[letter.lower()] += 1
        elif str.isalpha(letter):
            d1[letter.lower()] = 1
        else:
            continue

s1 = pd.Series(d1)

newfile = open('parta.txt', 'w')
newfile.write(str(s1[:]))
newfile.close()
## PART A

s1 = pd.Series(d1)

topTen = s1.sort_values(ascending=False)[:10]
str(topTen)
newfile2 = open('partb.txt', 'w')
newfile2.write(str(topTen))
newfile2.close()
## PART B

import string
d2 = {}
for entry in listAll:
    entry = entry.translate({ord(c): None for c in ",.<>?/;:()*&^%$#@!'-[]"})
    if entry.lower() in d2:
        d2[entry.lower()] += 1
    else:
        d2[entry.lower()] = 1

d2 = pd.Series(d2)
d2.sort_values(ascending=False).to_csv('partc.txt')
## PART C

file4 = open('partd.txt', 'w')
topTenWords = d2.sort_values(ascending=False)[:10]
file4.write(str(topTenWords))
file4.close()
## PART D

import string
dFile1 = {}
listStopWords = []
stopWords = open('stopwords.csv', 'r')
for entry in stopWords:
    listStopWords.append(entry.strip('\n'))

for entry in listFile1:
    if len(entry) <= 1:
        listFile1.remove(entry)

for entry in listFile1:
    entry = entry.translate({ord(c): None for c in ",.<>?/;:()*&^%$#@!'-[]`"})

    if entry.lower() in dFile1:
        dFile1[entry.lower()] += 1
    else:
        dFile1[entry.lower()] = 1

for entry in listStopWords:
    if entry in dFile1 :
        del dFile1[entry]

partE = pd.Series(dFile1)

partE = partE.sort_values(ascending=False)[:10]

file1Frequencies = {}

for index in partE.index:
    file1Frequencies[index] = partE[index]

file2Frequencies = {}

for entry in listFile2:
    entry = entry.translate({ord(c): None for c in ",.<>?/;:()*&^%$#@!'-[]`"})

    if entry.lower() in file2Frequencies:
        file2Frequencies[entry.lower()] += 1
    else:
        file2Frequencies[entry.lower()] = 1

for word in file2Frequencies:
    if word in partE.index:
       file1Frequencies[word] = file1Frequencies[word], file2Frequencies[word]

df1 = pd.Series(file1Frequencies,index=file1Frequencies.keys())

df1 = df1.apply(pd.Series)

df1.columns=['Script1', 'Script2']
df1.fillna(0)

file5 = open('parte.txt', 'w')
file5.write(str(df1.fillna(0)))
file5.close()

## PART E
