import streamlit as st
import pandas as pd

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['a', 'b', 'c'])

st.line_chard(chart_data)
