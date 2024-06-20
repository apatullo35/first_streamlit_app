import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase =lambda x: str(x).lower()
    data.rename(lowercase, axis= 'columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')

# df = pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# })

# df

# chart_data = pd.DataFrame(
# np.random.randn(20, 3),
# columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
# np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
# columns=['lat', 'lon'])

# st.map(map_data)

# x = st.slider('x') #
# st.write(x, 'squared is', x * x)

# st.text_input("Your name", key="name")

# st.session_state.name
