# import pands, streamlit, nd plotly

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('internet_users.csv')

# preparing the data
df['growth_rate'] = df['Internet Users'] / df.groupby("Country")('Internet Users').shift(1) -1

# setting up streamlit
st.title('Global Internet Usage Dashboard')

# navisgation sidebar

page = st.sidebar.selectbox("Choose a page", ["overview", "Disparities", "Growth Trends", "Importance of Internet Access" ])


