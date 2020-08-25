# Lines starting with # are comments and are not run by Python.
"""
Multi-line comments are possible with triple quotes like this.
"""
# pandas is a common library for working with data in Python, we usually import it like so:
import pandas as pd
import matplotlib.pyplot as plt

# This data comes from the UCI ML repository:
# https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# It is the daily number of users from a bike share program
df = pd.read_csv('day.csv')

# shows a preview of the data
df.head()
# shows some basic stats of the data
df.describe()

# Use the examples in the jupyter notebook to help you here.
# calculate the mean and standard deviation of the hourly data counts (the 'cnt' column)
# mean

hourly = df["cnt"]

print("Mean Deviation:", hourly.mean())

#___

# standard deviation

print("Standard Deviation:", hourly.std())

#___
# plot the counts ('cnt' column)

plt.plot(hourly)                      # create a plot of list generated
plt.xlabel("Hourly Count Length")     # label x axis
plt.ylabel("Hourly Count Values")     # label y axis
plt.title('Hourly Data Counts Plot')  # title the plot
plt.show()                            # show the plot

#___