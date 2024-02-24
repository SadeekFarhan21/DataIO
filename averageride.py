import pandas as pd
import plotly.express as px

# Define the directory path
data_directory = '/Users/aneeshsonnekar/Downloads/dataio/DataIO/'

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

# Convert 'started_at' and 'ended_at' columns to datetime objects with a flexible format
concatenated_df['started_at'] = pd.to_datetime(concatenated_df['started_at'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
concatenated_df['ended_at'] = pd.to_datetime(concatenated_df['ended_at'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Fill missing seconds with :00
concatenated_df['started_at'] = concatenated_df['started_at'].fillna(concatenated_df['started_at'].dt.floor('min'))
concatenated_df['ended_at'] = concatenated_df['ended_at'].fillna(concatenated_df['ended_at'].dt.floor('min'))

# Calculate ride durations in minutes
concatenated_df['ride_duration'] = (concatenated_df['ended_at'] - concatenated_df['started_at']).dt.total_seconds() / 60

# Calculate the average ride duration by user type
average_ride_duration_by_user_type = concatenated_df.groupby('member_casual')['ride_duration'].mean().reset_index()

# Plot the average ride duration by user type using Plotly with enhanced styling
fig = px.bar(average_ride_duration_by_user_type, x='member_casual', y='ride_duration',
             labels={'member_casual': 'User Type', 'ride_duration': 'Average Ride Duration (minutes)'},
             title='Average Ride Duration by User Type',
             color='member_casual', color_discrete_map={'casual': '#ADD8E6', 'member': '#FFB6C1'},  # Pastel colors
             template='plotly',  # Default plotly theme
             width=800, height=500,  # Adjust width and height
             text=average_ride_duration_by_user_type['ride_duration'].round(2),  # Add hover text
             
             )
fig.update_traces(texttemplate='%{text} minutes', textposition='outside')  # Position hover text
fig.update_layout(xaxis={'categoryorder': 'total descending'}, plot_bgcolor='white')  # Sort x-axis categories and set background color
fig.show()