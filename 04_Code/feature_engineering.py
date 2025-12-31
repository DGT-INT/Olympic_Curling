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

