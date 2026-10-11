import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = range(1880, 2051)
    ax.plot(
        years,
        [slope * year + intercept for year in years]
    )

    # Line of best fit from the year 2000 onward
    recent_df = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    recent_years = range(2000, 2051)
    ax.plot(
        recent_years,
        [
            slope_recent * year + intercept_recent
            for year in recent_years
        ]
    )

    # Set the title and axis labels
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save the plot
    fig.savefig('sea_level_plot.png')

    # Return the Axes object for the tests
    return ax