# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:07:37 2023

@author: Yamini Peri
"""

import pandas as pd
import matplotlib.pyplot as plt

# read the data file into a pandas dataframe
df = pd.read_csv("E:\iris data.csv")

# function to plot a bar chart of mean sepal length by species
def plot_sepal_bar(df):
    """
   Plot a bar chart of the mean sepal length for each species of iris.

   Args:
       df (pandas.DataFrame): A pandas dataframe containing the iris data.
   """
    # calculate the mean sepal length for each species
    setosa_mean = df[df['species'] == 'setosa']['sepal_length'].mean()
    versicolor_mean = df[df['species'] == 'versicolor']['sepal_length'].mean()
    virginica_mean = df[df['species'] == 'virginica']['sepal_length'].mean()
    
    # plot the data as a bar chart
    plt.bar(['setosa', 'versicolor', 'virginica'], [setosa_mean, versicolor_mean, virginica_mean])
    plt.title('Mean Sepal Length for Different Iris Species')
    plt.xlabel('Species')
    plt.ylabel('Mean Sepal Length')
    #plt.legend()
    plt.show()

# call the function to plot the data
plot_sepal_bar(df)
