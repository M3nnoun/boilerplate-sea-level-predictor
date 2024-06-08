import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = np.arange(df['Year'].min(), 2051)  # Use numpy to create array from 1880 to 2050
    y_pred1 = intercept1 + slope1 * x_pred1
    plt.plot(x_pred1, y_pred1, label='Best Fit Line 1', color='r')

    # Create second line of best fit for data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)  # Use numpy to create array from 2000 to 2050
    y_pred2 = intercept2 + slope2 * x_pred2
    plt.plot(x_pred2, y_pred2, label='Best Fit Line 2', color='g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return the axis for unit tests
    plt.savefig('sea_level_plot.png')
    return plt.gca()