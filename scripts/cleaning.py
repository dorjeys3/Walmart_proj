import numpy as np
import pandas as pd
from scipy import stats

# all fucntions for the projects live here
def drop_duplicates(df, columns):
    '''df = dataframe
        columns must be passed as string'''
    df.drop_duplicates(subset=columns, inplace=True)

# for processing noisy contineous values
def convertor(x):
    '''Converts string to a list and returns index 0'''
    #used to clean raw price column and num_rating column
    x = list(x.split(" "))
    return x[0]

def remove_perc(x):
    '''Converts string to a list and returns index 0'''
    #used to clean raw price column and num_rating column
    x = list(x.split("%"))
    return x[0]

def remove_dollar(x):
    x = list(x.split("$"))
    return x[1]

def bin_target(df, column):
    target = []
    for x in df[column]:
        if x >= 83:
            target.append(1)
        else:
            target.append(0)
    df["target"] = target

def bin_rating(df, column):
    rating_bin = []
    for x in df[column]:
        if x < 4:
            rating_bin.append(0)
        elif x >4.5:
            rating_bin.append(2)
        else:
            rating_bin.append(1)

    df["rating_bin"] = rating_bin

def cen_ten(df, columns):
    '''produces the mean, median and mode'''
    print(f"The median is {np.median(df[columns])}")
    print(f"The mean is {np.mean(df[columns])}")
    print(f"The mode is {stats.mode(df[columns])}")
