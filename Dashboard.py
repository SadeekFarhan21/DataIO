import pandas as pd
import plotly.express as px
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title='Team Janardhan',
    page_icon=":bar_chart:",
    layout="wide",
)

# Title and styling
st.title(':bar_chart: Bike Data Analytics')
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)

images = [
    ('000022.png', 'Number of Trips in 2023'),
    ('0000fa.png', 'Most popular routes'),
    ('000052.png', 'Number of trips throught the week'),
    ('000020.png', 'Average length of the trips during different months and seasons'),
    ('image.png', 'Top 20 longest rides'),
    ('avgdurationcool.png', 'Average duration of the rides'),
    ('peakhours2.png', 'Peak hours for the rides'),
    ('000010.png', 'Percent of trips across the seasons'),
    ('mostPopularStations.png', 'Most popular Stations'),
    ('0000fa.png', 'Most popular routes'),
    ('image.png', 'Top 20 longest rides'),
    ('avgdurationcool.png', 'Average duration of the rides'),
    ('peakhours2.png', 'Peak hours for the rides'),
    ('mostdestination.png', 'Most popular Destinations'),
    ('biketypes.png', 'Types of Bikes'),
    ('newplot.png', 'Distribution of Casual and Member Riders')
]
# number of trips
st.title('Number of Trips in 2023')
st.image('000022.png')

# precentage of trips in seasons
st.markdown('Most people bike during spring and summer')
st.title('Percent of Trips across differenet seasons')
st.image('000010.png')

# across the week
st.title('Number of trips on days of the week')
st.image('000052.png')

# average duration in the week
st.title('Average duration of the trips during the week')
st.image('avgdurationcool.png')
st.title('Most popular Stations')
st.image('mostPopularStations.png')
# starting location
st.title('Most popular starting locations')
import plotly.graph_objects as go
import pandas as pd
# Define the latitude and longitude coordinates
latitudes = [41.892278, 41.785097, 41.794301, 41.791478, 41.794301, 41.880958, 41.790000, 41.890000, 41.900960]
longitudes = [-87.612043, -87.601073, -87.601450, -87.599861, -87.601073, -87.616743, -87.600000, -87.650000, -87.623777]
# january = pd.read_csv('datasets/January.csv')
#february = pd.read_csv('datasets/February.csv')
#march = pd.read_csv('datasets/March.csv')
#april = pd.read_csv('datasets/April.csv')
#may = pd.read_csv('datasets/May.csv')
#june = pd.read_csv('datasets/June.csv')
#july = pd.read_csv('datasets/July.csv')
#august = pd.read_csv('datasets/August.csv')
#september = pd.read_csv('datasets/September.csv')
#october = pd.read_csv('datasets/October.csv')
#november = pd.read_csv('datasets/November.csv')
#december = pd.read_csv('datasets/December.csv')
#dataframes = [january, february, march, april, may, june, july, august, september, october, november, december]
# df = pd.concat(dataframes, ignore_index=True)
# Create a scatter plot trace for the coordinates
trace = go.Scattermapbox(
    lat = latitudes,
    lon = longitudes,
    mode = 'markers',
    marker = dict(
        size = 9,
        color = 'red',
        opacity = 0.7
    )
)

# Create the layout for the map
layout = go.Layout(
    mapbox = dict(
        style = 'open-street-map',  # Set the map style to OpenStreetMap
        center = dict(
            lat = 41.89,
            lon = -87.62
        ),
        zoom = 10
    ),
    height=800
)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Show the figure
st.plotly_chart(fig, use_container_width=True)


# most popular ending locations

st.title('Density Map of Ending Locations')
st.image('Ending_Locations.png')
st.image('mostdestination.png')
# peak hours
st.title('Peak hours during the day')
st.image('peakhourswhitebackground.png')
st.image('pkhr.png')
# Most popular routes

st.title('Most popular Stations')
st.image('mostPopularStations.png')

st.title('Most popular routes')
st.image('0000fa.png')

st.title('Type of Bikes')
st.image('biketypes.png')

st.title('Longest Ride')
st.image('longestride.png')

st.title('Distribution of Member and Casual')
st.image('newplot.png')


st.title('Stolen Bikes')
st.code('''
        
null_vals = df.isnull().sum()
null_vals
''')

st.code('''
start_lat                  0
start_lng                  0
end_lat                 5961
end_lng                 5961        
        ''')