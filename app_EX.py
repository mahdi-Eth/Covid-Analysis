# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# %%
df = pd.read_csv('owid-covid-data.csv')
df.drop(['Admin2','Province_State','FIPS','Recovered','Lat','Long_','Last_Update'], axis=1, inplace=True)

# %%
df.rename(columns={'Country_Region': 'Country', 'Combined_Key': 'Location'}, inplace=True)
df.dropna(inplace=True)

# %%
data_frame = pd.DataFrame(df,range(1,3450))
Top_8_Death_Countries = data_frame.sort_values('Deaths',ascending=False).head(8)

# %%
plt.bar(Top_8_Death_Countries['Country'],Top_8_Death_Countries['Deaths'],width=.65, color=['black','red','tomato','orange','yellow','green','blue','grey'])
plt.title('Top 8 Countries with most deaths')
plt.ylabel('Number of Deaths', fontsize=12)
plt.xlabel('Name of Countries', fontsize=12)
plt.show()


