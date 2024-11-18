

import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('path_to_your_file.csv')

# Display the first few rows to inspect
print(data.head())


'''
Removing missing values----------

# Drop rows with missing values
cleaned_data = data.dropna()

# Inspect the cleaned data
print(cleaned_data.head())


filtering rows based on condition----------------

# Filter rows where a column has values greater than a threshold
filtered_data = data[data['column_name'] > threshold_value]

# Inspect the filtered data
print(filtered_data.head())


aggregating data ------------------

# Group by a column and calculate sum for each group
grouped_data = data.groupby('group_column').sum()

# Inspect the grouped data
print(grouped_data.head())


'''


'''
# VISUALIZING DATA 
import matplotlib.pyplot as plt

# Create a bar chart
grouped_data['column_to_visualize'].plot(kind='bar')

# Add labels and title
plt.xlabel('Group')
plt.ylabel('Values')
plt.title('Bar Chart of Values by Group')

# Display the plot
plt.show()

'''


# EXPORTIN DATA TO CSV#
# Save the transformed data to a new CSV file
#cleaned_data.to_csv('cleaned_data.csv', index=False)
