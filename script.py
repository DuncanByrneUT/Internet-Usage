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

# Global Stats
if page == "Overview":
    st.subheader("Global Internet Usage Statistics")
    total_users = df['Internet Users'].sum()
    st.write(f"Total Internet Users Worldwide: {total_users:,}")
    avg_pen = df['Internet Penetration'].mean()
    st.write(f"Average Internet Penetration: {avg_pen:.2f}%")

    # global distribution plot
    fig = px.choropleth(df, locations="Country", locationmode='country names',
                        color='Internet Users', hover_name="Country",
                        title="Internet Users by Country")
    st.plotly_chart(fig)

# disparities
if page == "Disparities":
    st.subheader("Disparities in Intenet Usage")
    sorted_df = df.sort_values('Internet Penetration')
    fig = px.bar(sorted_df, x='Country', y='Internet Penetration',
                 title="Countries Ranked by Internet Penetration")
    st.plotly_chart(fig)

    st.write("Top 5 Countries with Lowest Internet Penetration:")
    st.write(sorted_df.head())

# growth trends