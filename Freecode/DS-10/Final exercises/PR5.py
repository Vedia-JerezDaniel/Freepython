import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


    df = pd.read_csv("E:\GitRepo\Freecode\DS-10\Final exercises\data\epa-see-level.csv")
  
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope, intercept, r_value, p_value, std_err = line1

    years_extended = df['Year'].append(pd.Series(range(2014, 2051)), ignore_index=True)
    # print(years_extended)

    plt.plot(years_extended, years_extended*slope + intercept, color="black")

    # Create second line of best fit
    mad = df['Year']>=2000
    line2 = linregress(df['Year'][mad], y = df['CSIRO Adjusted Sea Level'][mad])
    slope, intercept, r_value, p_value, std_err = line2
    years_reduced = years_extended[years_extended>=2000]
    plt.plot(years_reduced, years_reduced*slope + intercept, color="red")
    print(years_reduced*slope + intercept)
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


