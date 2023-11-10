
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns


# Specify the file path to your CSV file
file_path = r'D:\CBI_Solutions\2023\November\Balu\Time.csv'

# Load the CSV file into a pandas DataFrame
df_time = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to inspect the data
print(df_time.head())

# Extract the 'date,' 'confirmed,' 'released,' and 'deceased' columns
dates = pd.to_datetime(df_time['date'])  # Convert 'date' to datetime format
confirmed = df_time['confirmed']
released = df_time['released']
deceased = df_time['deceased']

# Create a line plot
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size

# Plot 'confirmed' cases
plt.plot(dates, confirmed, marker='o', linestyle='-', label='Confirmed')

# Plot 'released' cases
plt.plot(dates, released, marker='o', linestyle='-', label='Released')

# Plot 'deceased' cases
plt.plot(dates, deceased, marker='o', linestyle='-', label='Deceased')

# Format the date labels
date_format = DateFormatter("%Y-%m-%d")  # Define the date format
plt.gca().xaxis.set_major_formatter(date_format)  # Apply the date format

# Rotate x-axis labels for better visibility (optional)
plt.xticks(rotation=45)

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('COVID-19 Cases Over Time')

# Show a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()




# Load the 'TimeAge.csv' dataset
file_path = r'D:\CBI_Solutions\2023\November\Balu\TimeAge.csv'
time_age = pd.read_csv(file_path)

# Group the data by 'age' and calculate the sum of 'confirmed' and 'deceased' cases
age_group_data = time_age.groupby('age')[['confirmed', 'deceased']].sum().reset_index()

# Create a bar plot
plt.figure(figsize=(12, 6))

# Use Seaborn to create a bar plot
sns.barplot(data=age_group_data, x='age', y='confirmed', color='skyblue', label='Confirmed')
sns.barplot(data=age_group_data, x='age', y='deceased', color='salmon', label='Deceased')

plt.xlabel('Age Group')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Cases by Age Group')
plt.xticks(rotation=45)
plt.legend()

plt.show()



# Load the 'region.csv' dataset
file_path = r'D:\CBI_Solutions\2023\November\Balu\Region.csv'  # Replace with the actual file path
df_region = pd.read_csv(file_path)

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
plt.scatter(df_region['elderly_population_ratio'], df_region['academy_ratio'], alpha=0.5, color='b')

# Set plot labels and title
plt.xlabel('Elderly Population Ratio')
plt.ylabel('Nursing Home Count')
plt.title('Scatter Plot: Elderly Population Ratio vs. Nursing Home Count')

# Show the plot
plt.grid(True)
plt.show()




