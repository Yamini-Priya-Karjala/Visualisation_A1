# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 02:22:26 2023

@author: Yamini Peri
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_resident_population(data):
    """
    Plot a multi-line graph of resident population by state and year.
    
    Parameters:
    data (str): The file path of the CSV file containing the data.
    """
    plt.figure()
    # create a dataframe from the given data
    data = pd.read_csv("D:\Yamini Assignment\state population.csv")

    # convert Resident Population column from string to integer
    data['Resident Population'] = data['Resident Population'].str.replace(',', '').astype(int)

    # pivot the dataframe to create a multi-index for plotting
    data_pivot = data.pivot(index='Year', columns='State', values='Resident Population')

    # plot the multi-line graph
    data_pivot.plot(kind='line', marker='o')
    plt.title('Resident Population by State and Year')
    plt.xlabel('Year')
    plt.ylabel('Resident Population')
    plt.legend()
    plt.show()

# calling the function
plot_resident_population('D:\Yamini Assignment\state population.csv')
