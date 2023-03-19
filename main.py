#=================================================================================#
#                                 FASTAPI                                         #
#=================================================================================#
# libraries
from fastapi import FastAPI
import numpy as np
import pandas as pd
#---------------------------------------------------------------------------------#
# data
data = pd.read_csv('data/data.csv')
#---------------------------------------------------------------------------------#
# instance of the FastAPI class
app = FastAPI()
#---------------------------------------------------------------------------------#
# main rute (root function)
@app.get('/')
async def root():
    return 'welcome'
#---------------------------------------------------------------------------------#
# get_max_duration function:
@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
async def get_max_duration(year, platform, duration_type):
    df_f1 = data[data['release_year'] == int(year)] 
    df_f2 = df_f1[df_f1['id'].str[0] == platform[0].lower()]
    df_f3 = df_f2[df_f2['duration_type'] == duration_type]
    max = df_f3['duration_int'].astype('int64').max()

    # It could be more than one movie with max duration_int
    df_result = df_f3[df_f3['duration_int'] == max]

    titles = []

    for element in df_result['title']:
        titles.append(element)

    return titles
#---------------------------------------------------------------------------------#
# get_score_count function:
@app.get('/get_score_count/{platform}/{scored}/{year}')
def get_score_count(platform, scored, year):
    df_f1 = data[data['id'].str[0] == platform[0].lower()]
    df_f2 = df_f1[df_f1['score'] > float(scored)]
    df_f3 = df_f2[df_f2['release_year'] == int(year)]
    df_f4 = df_f3[df_f3['type'] == 'movie']

    return len(df_f4)
#---------------------------------------------------------------------------------#
# get_count_platform function:
@app.get('/get_count_platform/{platform}')
def get_count_platform(platform):
    df_f1 = data[data['id'].str[0] == platform[0].lower()]
    df_f2 = df_f1[df_f1['type'] == 'movie']

    return len(df_f2)
#---------------------------------------------------------------------------------#
# Documentation used for queries
'''
https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html
'''
#=================================================================================#