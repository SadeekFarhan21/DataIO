import pandas as pd
import plotly.express as px

data_directory = '/Users/aneeshsonnekar/Downloads/dataio/DataIO/'

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

concatenated_df = pd.concat([january_df, february_df, march_df, april_df, may_df, june_df, july_df, august_df, september_df, october_df, november_df, december_df], ignore_index=True)

percent_sample = 0.1 
sample_size = int(len(concatenated_df) * percent_sample)

random_sample = concatenated_df.sample(n=sample_size)




rideable_type_counts = random_sample['rideable_type'].value_counts()

colors = ['#ADD8E6', '#FFA07A', '#90EE90']

fig = px.pie(rideable_type_counts, values=rideable_type_counts.values, names=rideable_type_counts.index, 
             title='Rideable Type Distribution', color_discrete_map={rideable_type_counts.index[i]: colors[i] for i in range(len(colors))})


fig.update_traces(marker=dict(colors=colors))

fig.show()