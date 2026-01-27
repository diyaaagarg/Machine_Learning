import streamlit as st
import pandas as pd
import numpy as np

#title of application
st.title("hello streamlit")

#display a simple text
st.write("this is streamlit course")

#create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4], 
    'second column': [10, 20, 30, 40]})
#display the data frame
st.write('Here is the data frame:')
st.write(df)

#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)