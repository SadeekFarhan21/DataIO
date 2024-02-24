import pandas as pd
import plotly.express as px
import datetime


# Define the directory path
data_directory = 'DATAIO/'

# Load datasets for each month with updated file paths
january_df = pd.read_csv(data_directory + 'January.csv')
february_df = pd.read_csv(data_directory + 'February.csv')
march_df = pd.read_csv(data_directory + 'March.csv')
april_df = pd.read_csv(data_directory + 'April.csv')
may_df = pd.read_csv(data_directory + 'May.csv')
june_df = pd.read_csv(data_directory + 'June.csv')
july_df = pd.read_csv(data_directory + 'July.csv')
august_df = pd.read_csv(data_directory + 'August.csv')
september_df = pd.read_csv(data_directory + 'September.csv')
october_df = pd.read_csv(data_directory + 'October.csv')
november_df = pd.read_csv(data_directory + 'November.csv')
december_df = pd.read_csv(data_directory + 'December.csv')

# Concatenate all datasets
concatenated_df = pd.concat([january_df, february_df, march_df, april_df, may_df, june_df, july_df, august_df, september_df, october_df, november_df, december_df], ignore_index=True)

# Optionally, handle duplicates or missing values
# concatenated_df.drop_duplicates(inplace=True)

# Inspect the concatenated dataset



# Define possible datetime formats
datetime_format = ["%m/%d/%y %H:%M:%S", "%m/%d/%y %H:%M"]




# Assuming 'concatenated_df' contains your concatenated dataset

# Print the DataFrame before conversion


# Assuming 'concatenated_df' contains your concatenated dataset

datetime_format = "%Y-%m-%d %H:%M:%S"

# Convert 'started_at' and 'ended_at' columns to datetime objects
concatenated_df['started_at'] = pd.to_datetime(concatenated_df['started_at'], format=datetime_format, errors='coerce')
concatenated_df['ended_at'] = pd.to_datetime(concatenated_df['ended_at'], format=datetime_format, errors='coerce')

# Print the DataFrame after conversion
print("DataFrame after conversion:")
print(concatenated_df.head())

# Extract hour from 'started_at' and 'ended_at' columns
concatenated_df['start_hour'] = concatenated_df['started_at'].dt.hour
concatenated_df['end_hour'] = concatenated_df['ended_at'].dt.hour

# Print some information to check
print("Number of rows after conversion:", len(concatenated_df))
print("Unique values of 'member_casual':", concatenated_df['member_casual'].unique())

# Group by 'start_hour' and 'member_casual', then sum the counts
hourly_counts = concatenated_df.groupby(['start_hour', 'member_casual']).size().reset_index(name='count')

# Print the grouped data to check
print("Grouped data:")
print(hourly_counts)

# Plot using Plotly
fig = px.bar(hourly_counts, x='start_hour', y='count', color='member_casual', 
             labels={'start_hour': 'Hour', 'count': 'Total Users', 'member_casual': 'User Type'},
             title='Peak Hours for Members and Casuals')
fig.show()




