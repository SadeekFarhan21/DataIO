import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Create some sample data
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

# Define the Streamlit app
def main():
    st.title('Streamlit App with Plotly Graphs')

    # First container with some text
    with st.container():
        st.header('Container 1: Introduction')
        st.write('Welcome to the Streamlit app!')

    # Second container with a Plotly scatter plot
    with st.container():
        st.header('Container 2: Scatter Plot')
        fig_scatter = px.scatter(df, x='x', y='y', color='category')
        st.plotly_chart(fig_scatter)

    # Third container with a Plotly histogram
    with st.container():
        st.header('Container 3: Histogram')
        fig_histogram = px.histogram(df, x='x', color='category', marginal='rug')
        st.plotly_chart(fig_histogram)

    # Fourth container with a Plotly bar chart
    with st.container():
        st.header('Container 4: Bar Chart')
        df_grouped = df.groupby('category').size().reset_index(name='counts')
        fig_bar = px.bar(df_grouped, x='category', y='counts', color='category')
        st.plotly_chart(fig_bar)

if __name__ == '__main__':
    main()
