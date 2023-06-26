import pandas as pd
import streamlit as st
import pygwalker as pyg


st.set_page_config(layout="wide")

st.header("MY SECOND PROJECT ")





def load_data(url):
    df = pd.read_csv(url)

    return df
df = load_data("C:\Users\rumma\PycharmProjects\pythonProject15\bangalore.csv")



def display(con):

    with open(con,"r") as f:
        file = f.read()
    return file
file = display("C:\Users\rumma\Desktop\config.json")
pyg.walk(df,env="Streamlit",spec=file,dark="light")

