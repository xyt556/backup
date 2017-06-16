import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt

# Here you put your code to read the CSV-file into a DataFrame df
df = pandas.read_csv("test2.csv")
plt.figure(figsize=(7,5)) # Set the size of your figure, customize for more subplots

for i in range(len(df)):
    xs = np.array(df[df.columns[0::2]])[i] # Use values from odd numbered columns as x-values
    ys = np.array(df[df.columns[1::2]])[i] # Use values from even numbered columns as y-values
    plt.subplot(len(df), 1, i+1)
    plt.plot(xs, ys, marker='o') # Plot circle markers with a line connecting the points
    for j in range(len(xs)):
        plt.annotate(df.columns[0::2][j][-3:] + '"', # Annotate every plotted point with last three characters of the column-label
                     xy = (xs[j],ys[j]),
                     xytext = (0, 5),
                     textcoords = 'offset points',
                     va = 'bottom',
                     ha = 'center',
                     clip_on = True)
    plt.title('Spectral class ' + df.index[i])
    plt.xlabel('Limiting Magnitude')
    plt.ylabel('Exposure Time')
    plt.grid(alpha=0.4)

plt.tight_layout()
plt.show()