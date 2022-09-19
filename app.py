import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px



df = pd.read_csv('owid-covid-data.csv')

df.drop(['FIPS','Admin2','Province_State','Last_Update','Combined_Key'],axis=1,inplace=True)
df.rename(columns={'Country_Region': 'Country'},inplace=True)
world_grouped_by =  df.groupby('Country')['Confirmed','Active','Recovered','Deaths'].sum().reset_index()

