import streamlit as st
import pandas as pd
st.title("Streamlit test Input")
name=st.text_input("enter your name:")
age=st.slider("select your age :",0,100,25)
st.write(f"your ageis {age}.")
options = ['Python', 'Java', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language', options)
st.write(choice)
if name:
    st.write(f"hello,{name}")

data={
    "name":["john","jane","diya"],
    "age":[23,32,23]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("chhose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)