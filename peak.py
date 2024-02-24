import pandas as pd
import plotly.express as px
import datetime

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

# Convert 'started_at' and 'ended_at' columns to datetime objects
concatenated_df['started_at'] = pd.to_datetime(concatenated_df['started_at'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
concatenated_df['ended_at'] = pd.to_datetime(concatenated_df['ended_at'], format='%Y-%m-%d %H:%M:%S', errors='coerce')



# Extract hour from 'started_at' and 'ended_at' columns
concatenated_df['start_hour'] = concatenated_df['started_at'].dt.hour
concatenated_df['end_hour'] = concatenated_df['ended_at'].dt.hour

# Group by 'start_hour' and 'member_casual', then sum the counts
hourly_counts = concatenated_df.groupby(['start_hour', 'member_casual']).size().reset_index(name='count')
# Convert military time to normal time format in the hourly_counts DataFrame
hourly_counts['start_hour'] = pd.to_datetime(hourly_counts['start_hour'], format='%H').dt.strftime('%I %p').str.lstrip('0') 

# Plot using Plotly with pastel color scheme
fig = px.bar(hourly_counts, x='start_hour', y='count', color='member_casual', 
             labels={'start_hour': 'Hour', 'count': 'Total Users', 'member_casual': 'User Type'},
             title='Peak Hours for Members and Casuals',
             color_discrete_map={'casual': '#ADD8E6', 'member': '#FFB6C1'},  # Pastel colors
             )
fig.show()

fig.update_layout(
    title={'text': 'Peak Hours for Members and Casuals', 'font_size': 24},  # Title font size
    xaxis_title='Hour',  # X-axis title
    yaxis_title='Total Users',  # Y-axis title
    font=dict(size=18)  # Font size for axes titles
)

fig.show()