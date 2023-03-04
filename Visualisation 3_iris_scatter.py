# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:31:16 2023

@author: Yamini Peri
"""

import pandas as pd
import matplotlib.pyplot as plt

# read the data file into a pandas dataframe
df = pd.read_csv("E:\iris data.csv")

# function to plot a scatter plot of petal length vs. petal width, colored by species
def plot_petal_scatter(df):
    
    """
   plots a scatter plot of petal length vs. petal width, colored by species.

   Args:
       df: pandas dataframe containing the Iris dataset

   Returns:
       None
   """
    # create separate dataframes for each species
    setosa_df = df[df['species'] == 'setosa']
    versicolor_df = df[df['species'] == 'versicolor']
    virginica_df = df[df['species'] == 'virginica']
    # plot the data as a scatter plot with different colors for each species
    plt.scatter(setosa_df['petal_length'], setosa_df['petal_width'], label='setosa')
    plt.scatter(versicolor_df['petal_length'], versicolor_df['petal_width'], label='versicolor')
    plt.scatter(virginica_df['petal_length'], virginica_df['petal_width'], label='virginica')
    plt.title('Petal Length vs. Petal Width for Different Iris Species')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.show()

# call the function to plot the data
plot_petal_scatter(df)





