import pandas as pd
import streamlit as st
import plotly.express as px

import get_data

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Stop and Search",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# st.dataframe(df_city)

siteHeader = st.container()
first_column, second_column, third_column, fourth_column = st.columns(4)
reasonVisualization = st.container()

df_availability = get_data.get_availability_data()
df_dates = df_availability["date"].unique()

# ----- SIDEBAR --------------------------------
st.sidebar.header("Please, filter the report here:")
date_of_report = st.sidebar.selectbox(
    "Select a date:",
    options=df_dates
)

df_city = df_availability["stop-and-search"]

city_in_report = st.sidebar.selectbox(
    "Select a City:",
    options=df_city[0]
)

year, month = date_of_report.split('-')

#st.sidebar.write(year +"    "+ month)

df = get_data.generate_df(month, year, city_in_report)

with siteHeader:
    st.title(":bar_chart: Welcome to my first "
             "data analysis project!")
    st.text("In this project I look into stop and search data provided by UK Police")
    st.markdown("##")

total_stop_and_search = len(df)
arrests_made = len(df.query("outcome == 'Arrest'"))  # int(df["outcome"])
percentage_of_arrest = (arrests_made/total_stop_and_search)*100

with first_column:
    st.subheader(f"Total Stop and Search for")
    st.subheader(f"{city_in_report}")
    st.subheader(f"{total_stop_and_search}")

with second_column:
    st.subheader(f"Arrests")
    st.subheader(str(round(percentage_of_arrest, 2)) + "%")

with third_column:
    st.subheader(f"No Action Taken")
    st.subheader(str(round(percentage_of_arrest, 2)) + "%")


st.markdown("---")

with reasonVisualization:
    st.dataframe(df)
    # st.header('Dataset: Police Stop and Search Data')
    # st.text('I found this dataset at https://data.police.uk/')
    #reason_data = pd.DataFrame(df['gender'].value_counts())
    #st.bar_chart(reason_data)
    # st.dataframe(total_stop_and_search)
    # st.dataframe(arrests_made)
    # st.write(total_stop_and_search)
    # st.write(arrests_made)

