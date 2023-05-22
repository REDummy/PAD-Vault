import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv("winequality-white.csv", sep=";")

print(df.describe())

#plot - pair plot
seaborn.pairplot(df)
plt.show()
seaborn.lineplot(x="citric acid", y="quality", data=df)
plt.show()


# Console - Correlation matrix
correlation = df.corr(method='kendall')
print("\nCorrelation Matrix:")
print(correlation)

# plot - kde density
df['alcohol'].plot.kde()
plt.show()

# plot - semi 3d mapping between 3 values
df.plot.scatter(x='citric acid',y='alcohol',c='quality',cmap='coolwarm')
plt.show()

# console - testing out sorting
print("Descending Sorting based on quality")
df.sort_values("quality", axis = 0, ascending = False,
                 inplace = True, na_position ='last')

print(df.head())

# console - missing values
print("\nMissing value : ")
missing_values = df.isnull().sum()
print(missing_values)

#plot - quality bar
quality_counts = df['quality'].value_counts()

# Create a bar chart
plt.bar(quality_counts.index, quality_counts.values)

# Set the labels and title
plt.xlabel('Quality')
plt.ylabel('Count')
plt.title('Wine Quality Distribution')

# Display the chart
plt.show()

# Create a pie plot
plt.pie(quality_counts, labels=quality_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Quality')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the plot
plt.show()

# Extract the 'alcohol' column
alcohol_column = df['alcohol']

# Define the bins for alcohol levels
bins = [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20]

# Create a histogram of alcohol levels
alcohol_counts, _ = np.histogram(alcohol_column, bins=bins)

# Define the labels for the pie plot
labels = ['0-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-20']

# Create a pie plot
plt.pie(alcohol_counts, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of Alcohol Levels')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the plot
plt.show()