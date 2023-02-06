import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter("Year","CSIRO Adjusted Sea Level",data=df)
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")
    # Create first line of best fit
    lineA = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_valsA = np.arange(min(df['Year']),2051,1)
    y_valsA =x_valsA*lineA.slope+ lineA.intercept
    plt.plot(x_valsA,y_valsA)
    # Create second line of best fit
    df2000 = df[df['Year']>=2000]
    lineB = linregress(df2000['Year'],df2000['CSIRO Adjusted Sea Level'])
    x_valsB = np.arange(2000,2051,1)
    y_valsB = x_valsB*lineB.slope + lineB.intercept
    plt.plot(x_valsB,y_valsB)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()