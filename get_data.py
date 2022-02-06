from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import json


def get_availability_data():
    """
    Use the avalability API - https://data.police.uk/docs/method/crimes-street-dates/
    to get the a list of available data sets
    :return:
    """
    # data = json.dumps(requests.get("https://data.police.uk/api/crimes-street-dates"))
    # data = requests.get("https://data.police.uk/api/crimes-street-dates")
    data = json.loads(requests.get("https://data.police.uk/api/crimes-street-dates").text)
    # flattening json data
    df_availability = pd.json_normalize(data)
    # df_force.sort_values(by="datetime", inplace=True, ascending=True)
    # print(df_availability)

    return df_availability


# define an auxiliary function that will help in generating the dataframes
def generate_df(month, year, force):
    """ auxiliary function that helps to generate the main dataframes from the api url"""
    data = json.loads(requests.get(
        "https://data.police.uk/api/stops-force?force=" + force + "&date=" + str(year) + "-" + str(month)).text)

    # flattening json data
    df_force = pd.json_normalize(data)
    df_force.sort_values(by="datetime", inplace=True, ascending=True)
    df_force['force'] = str(force)
    df_force["year_month"] = df_force["datetime"].str[:7]
    # print(df_force.head())

    return df_force


#dfr = get_availability_data()
#
#print(dfr['date'].unique())
