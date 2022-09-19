import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


df = pd.read_csv('owid-covid-data.csv')


print(df.describe())
