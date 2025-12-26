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
df_games = pd.read_csv('../03_Data/Games.csv')
print(df_games.shape)
print(df_games.head())
print(df_games.tail())

# %%
cols = [
    'CompetitionID', 'SessionID', 'GameID', 'GroupID', 'Sheet',
    'NOC1', 'NOC2', 'LSFE', 'Winner', 'TeamID1', 'TeamID2'
]

df_games[cols].nunique()

# %%
df_games.isna().sum()

# %%
df_games.duplicated(subset=['SessionID', 'GameID', 'CompetitionID']).any()

# %%
# checking the Stones data
df_stones = pd.read_csv('../03_Data/Stones.csv')
print(df_stones.shape)
print(df_stones.head())
print(df_stones.tail())

# %%
df_stones.columns

# %%
print(len(df_stones['Task'].unique()))

# %%
# checking the Teams data
df_teams = pd.read_csv('../03_Data/Teams.csv')
print(df_teams.shape)
print(df_teams.head())
print(df_teams.tail())

# %%
cols = df_teams.columns.tolist()

df_teams[cols].nunique()

# %%
df_teams['NOC'].value_counts(dropna=False)

# %%
df_teams['Name'].value_counts(dropna=False)
# %%
