import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px



df = pd.read_csv('owid-covid-data.csv')

print(df)
print(df.shape)


# df.dropna(axis=0,inplace=True)

# print(df.head(1))
# print(df.shape)


