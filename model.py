
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import collections
import itertools

def rename_columns(df):
    #easier to type
    col_key = {'Unnamed: 0': 'id',
           'Months since Last Donation': 'months_since_last',
                        'Number of Donations': 'num_donations',
                        'Total Volume Donated (c.c.)': 'total_vol_donated',
                        'Months since First Donation': 'months_since_first',
                        'Made Donation in March 2007': 'donated'}
    df.rename(columns = col_key , inplace = True)
    return df

def add_features(df_raw):
    df = df_raw.copy()
    #Add frequency (donations in active period)
    df['frequency'] = df['num_donations']/(1+df['months_since_first']-df['months_since_last'])
    #Add month ratio-- smaller = wider active range,
    df['month_ratio'] = (df['months_since_last'])/(df['months_since_first'])
    df.drop(columns = ['total_vol_donated'], axis = 1, inplace = True)
    return df

def load_data(filename):
    df_raw = pd.read_csv(filename)
    rename_columns(df_raw)
    df = add_features(df_raw)
    return df

if __name__=='__main__':
    filename = "data/train.csv"
    df = load_data(filename)
    y = df.pop('donated')
    X = df
