import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("winequality-red.csv", sep=";")

# Basic statistics
statistics = df.describe()
print("\nStatistics:")
print(statistics)

# # Correlation matrix
# correlation = df.corr(method='kendall')
# print("\nCorrelation Matrix:")
# print(correlation)

# # kde density that doesnt make that much sense
# df['alcohol'].plot.kde()
# plt.show()

# # semi 3d mapping between 3 values
# df.plot.scatter(x='pH',y='alcohol',c='quality',cmap='coolwarm')
# plt.show()

# # testing out sorting
# df.sort_values("quality", axis = 0, ascending = False,
#                  inplace = True, na_position ='last')

# print(df.head())



# Plot is wayy to broad and can't be seen nicely
# plt.style.use('ggplot')
# df.plot.area(alpha=0.5)
# plt.show()

# # missing values
# missing_values = df.isnull().sum()

# print(missing_values)

# quality_counts = df['quality'].value_counts()

# # Create a bar chart
# plt.bar(quality_counts.index, quality_counts.values)

# # Set the labels and title
# plt.xlabel('Quality')
# plt.ylabel('Count')
# plt.title('Wine Quality Distribution')

# # Display the chart
# plt.show()