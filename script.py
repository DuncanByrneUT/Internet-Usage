# import pands, streamlit, nd plotly

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('CSV/internet_users.csv')
print(df.columns)  # Check to ensure these are the exact column names


# preparing the data
df['growth_rate'] = df['Users (CIA)'] / df.groupby('Location')['Users (CIA)'].shift(1) - 1

# setting up streamlit
st.title('Global Internet Usage Dashboard')

# navisgation sidebar

page = st.sidebar.selectbox("Choose a page", ["overview", "Disparities", "Growth Trends", "Importance of Internet Access" ])

# Global Stats
if page == "Overview":
    st.subheader("Global Internet Usage Statistics")
    total_users = df['Users (CIA)'].sum()
    st.write(f"Total Internet Users Worldwide: {total_users:,}")
    avg_pen = df['Internet Penetration'].mean()
    st.write(f"Average Internet Penetration: {avg_pen:.2f}%")

    # global distribution plot
    fig = px.choropleth(df, locations="Location", locationmode='country names',
                        color='Users (CIA)', hover_name="Location",
                        title="Internet Users by Country")
    st.plotly_chart(fig)

# disparities
if page == "Disparities":
    st.subheader("Disparities in Intenet Usage")
    sorted_df = df.sort_values('Rate (WB)')  # or whichever column represents penetration
    fig = px.bar(sorted_df, x='Location', y='Rate (WB)',  # or 'Rate (ITU)'
                 title="Locations Ranked by Internet Penetration")
    st.plotly_chart(fig)

    st.write("Top 5 Countries with Lowest Internet Penetration:")
    st.write(sorted_df.head())

# growth trends

if page == "Growth Trends":
    st.subheader("Internet Usage Growth Trends")
    if 'growth_rate' in df.columns:
        fig = px.scatter(df, x='Year', y='growth_rate', color='Location',
                         title="Internet Usage Growth by Location")
        st.plotly_chart(fig)
    else:
        st.write("Growth data not available. Please ensure your dataset includes multi-year data.")

# educational content

if page == "Importance of Internet Access":
    st.subheader("The Importance of Internet Access")
    st.write("Internet access plays a crucial role in education, economy, health, and social connectivity. Here's why:")
    st.markdown("""
    - **Education:** Online learning platforms provide education to remote areas.
    - **Economy:** Businesses leverage the internet for growth, marketing, and operations.
    - **Health:** Telemedicine and health information access improve healthcare outcomes.
    - **Social Connectivity:** Reduces isolation, especially in rural or disadvantaged communities.
    """)

    # Add some illustrative charts or images here if available or relevant