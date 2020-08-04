# dependencies:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\final_prep')

# 1. write a function that takes a file name as input, reads the csv file and returns a Pandas dataframe
def fileParser(filename):
    return(pd.read_csv(filename, low_memory=False))

# 2. Add a column named IsArtsy that contains one of two values, “Artsy” or “Not Artsy”, depending on whether one or more of the words in the field FavouriteActivity, belongs to the set of words contained in the file art.csv.

# we create a list of all the words in art.csv, column 1 ('ART')
artWords = list(fileParser('art.csv')['ART'])

# we read the dataset
df = fileParser('dataset.csv')
# create column IsArtsy with all values False(Not Artsy)
df['IsArtsy'] = 'Not Artsy'

# for every word that is artistic, if the word is in FavoriteActivity, IsArtsy will switch to Artsy
for word in artWords:
    df['IsArtsy'][df['FavouriteActivity'].str.contains(word)] = 'Artsy'
df['IsArtsy']
# 3. In two or three sentences, answer whether there is a difference between the average love of nature based on whether someone is artsy or not? Please provide numerical and graphical outputs (including a proper title, and X and Y axis titles) in support of your answer. Please save the grap	h as a png file and then as a pdf file.
flatui = ["#3498db", "#e74c3c"] # blue and red
sns.set_palette(flatui)
sns.set_style('darkgrid')
sns.boxplot(x='IsArtsy', y='LoveNature',data = df, saturation=.65, width=.6,notch=True)

# Sebastián Pastor Ferrari - 2019 ©
