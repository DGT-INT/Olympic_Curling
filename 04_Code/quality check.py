#%%
import numpy as np
import pandas as pd
import os

#%%
print(os.getcwd())

#%%
# checking the competition data
df_competition = pd.read_csv('../03_Data/Competition.csv')
print(df_competition.head())
print(df_competition.shape)

#%%
# checking the competitotrs data
df_competitors = pd.read_csv('../03_Data/Competitors.csv')
print(df_competitors.head())
print(df_competitors.shape)
print(df_competitors.tail())

# %%
print(len(df_competitors['CompetitionID'].unique()))
print(len(df_competitors['TeamID'].unique()))
print(len(df_competitors['NOC'].unique()))
print(len(df_competitors['Reportingname'].unique()))

# %%
df_competitors.isna().sum()

# %%
df_competitors.duplicated().any()
# %%
df_competitors.duplicated(subset=['CompetitionID', 'Reportingname']).sum()

# %%

# %%
