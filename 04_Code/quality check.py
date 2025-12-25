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
# checking the Ends data
df_ends = pd.read_csv('../03_Data/Ends.csv')
print(df_ends.shape)
print(df_ends.head())
print(df_ends.tail())

# %%
print(len(df_ends['CompetitionID'].unique()))

# %%
print(len(df_ends['SessionID'].unique()))
print(df_ends['SessionID'].unique())
# SessionID is not relevant for our analysis so I wont spend too much effort looking into it.

# %%
print(len(df_ends['GameID'].unique()))
print(len(df_ends['TeamID'].unique()))
print(len(df_ends['EndID'].unique()))
print(df_ends['EndID'].unique())

# %%
print(len(df_ends['Result'].unique()))
print(df_ends['Result'].unique())
print(df_ends['Result'].describe())
print((df_ends['Result'] > 1).sum())

# %%
1253/5274 # about 24% of the ends have a result greater than 1

# %%
print(len(df_ends['PowerPlay'].unique()))
print(df_ends['PowerPlay'].describe())

# %%
598/5274 # about 11% of the ends are power plays

# %%
df_ends['PowerPlay'].value_counts(dropna=False)

# %%
print(313/598) # about 52% of the power plays placed the starting stones on the right
print(285/598) # about 48% of the power plays placed the starting stones on the left 

# %%
# checking the Games data
# checking the Stones data
# checking the Teams data