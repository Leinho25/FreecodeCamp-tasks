import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    f,ax= plt.subplots(figsize=(20,10))
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"],color="g",label="Adjusted Sea Level")

    # Create first line of best fit
    reg=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    x=df["Year"]
    x_extended=np.arange(min(x),2051)
    plt.plot(x_extended,reg.intercept+reg.slope*x_extended, ls='--',c="r",label="Line of the best fit")
    # Create second line of best fit
    df2=df[df["Year"]>=2000]
    x2=df2["Year"]
    x2_extended=np.arange(min(x2),2051)
    reg2=linregress(df2["Year"],df2["CSIRO Adjusted Sea Level"])
    plt.plot(x2_extended,reg2.intercept+reg2.slope*x2_extended, ls='--',c="k",label="Line of the best fit since 2000")
    # Add labels and title
    plt.legend(loc="upper left")
    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()