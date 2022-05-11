import pandas as pd
import numpy as np

ranges = [[0.408, 0.503], [84.2, 120.1], [0, 5]]
corrs = [0.395, 0.349, 0.453, 0.169, 0.153, 0.431, 0.023, 0.004, 0.137, 0.124, 0.048, 0.083]

def cleanup(df):
    normalize = ['HOME_inj', 'AWAY_inj', 'H_FG_pct', 'A_FG_pct',  'H_PPG', 'A_PPG']
    scaled = df.copy()
    for index, row in scaled.iterrows():
        scaled.at[index, 'HOME_inj'] = (row['HOME_inj'] - ranges[0][0]) / (ranges[0][1] - ranges[0][0])
        scaled.at[index, 'AWAY_inj'] = (row['AWAY_inj'] - ranges[0][0]) / (ranges[0][1] - ranges[0][0])
        scaled.at[index, 'H_FG_pct'] = (row['H_FG_pct'] - ranges[1][0]) / (ranges[1][1] - ranges[1][0])
        scaled.at[index, 'A_FG_pct'] = (row['A_FG_pct'] - ranges[1][0]) / (ranges[1][1] - ranges[1][0])
        scaled.at[index, 'H_PPG'] = (row['H_PPG'] - ranges[2][0]) / (ranges[2][1] - ranges[2][0])
        scaled.at[index, 'A_PPG'] = (row['A_PPG'] - ranges[2][0]) / (ranges[2][1] - ranges[2][0])

    biased = scaled.copy()

    columns = biased.columns.to_numpy().tolist()

    for index, column in enumerate(columns):
        biased[column] = corrs[index] * biased[column]

    return biased
