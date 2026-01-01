#%%
import pandas as pd
import numpy as np

#%%
stones_data = pd.read_csv('../03_Data/Stones.csv')
stones_data.head()

# %%
# creating a new feature 'defensive_intent' based on the 'Task' column
positioning_tasks = [0, 1, 2, 5]
removal_tasks = [3, 4, 6, 7, 8, 9, 10]
ignored_tasks = [11, 13]

stones_data['defensive_intent'] = np.select(
    [
        stones_data['Task'].isin(positioning_tasks),
        stones_data['Task'].isin(removal_tasks),
        stones_data['Task'].isin(ignored_tasks)
    ],
    [
        'positioning',
        'removal',
        'ignored'
    ],
    default=None
)

stones_data['defensive_intent'].value_counts(dropna=False)
# %%
stones_data[stones_data['defensive_intent'].isna()].head()
# %%
stones_data.loc[stones_data['defensive_intent'].isna(),
                'Task'].value_counts()

# I am finding -1 in task, however i am not sure what is means. its not in the data dictionary
# %%
# creating a end-level table

# columns should be is_power_play, defensing_team, defensive_posutre

# random samples to understand the data
print(stones_data.shape)
n_rows = len(stones_data)
random_index = np.random.randint(0, n_rows)
stones_data.iloc[random_index]
start_index = np.random.randint(0, n_rows - 30)
stones_data.iloc[start_index:start_index + 30]

# %%
stones_data.head(30)

# %%
shots_by_team = ['CompetitionID', 'SessionID', 'GameID', 'EndID', 'TeamID']
stones_data['defensive_intent_shot1'] = stones_data.groupby(shots_by_team)['defensive_intent'].transform('first')
stones_data.head(30)

# %%
cols_to_show = list(stones_data.loc[:, 'CompetitionID':'Task'].columns) + ['defensive_intent', 'defensive_intent_shot1']
stones_data[cols_to_show].head(30)

# %%
stones_data['defensive_intent'].value_counts(normalize=True) *100

# %%
stones_data['defensive_intent_shot1'].value_counts(normalize=True)* 100

# %%
stones_data['defensive_intent_shot2'] = (
    stones_data.groupby(shots_by_team)['defensive_intent']
    .transform(lambda x: x.iloc[1] if len(x) > 1 else None)
)

cols_to_show = list(stones_data.loc[:, 'CompetitionID':'Task'].columns) + ['defensive_intent', 'defensive_intent_shot1', 'defensive_intent_shot2']
stones_data[cols_to_show].head(30)

# %%
stones_data['defensive_intent_shot2'].value_counts(normalize=True)*100

# %%
stones_data['defensive_structure'] = stones_data['defensive_intent_shot1'] + '-' + stones_data['defensive_intent_shot2'].fillna('none')
stones_data['defensive_structure'].value_counts(normalize=True)*100

# %%


# %%
