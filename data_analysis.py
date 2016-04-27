'''
    Johan Oakes
    April, 26, 2016
    soccer_analysis

    Dataset:

    Date = Match Date (dd/mm/yy)
    HomeTeam = Home Team
    AwayTeam = Away Team
    FTHG = Full Time Home Team Goals
    FTAG = Full Time Away Team Goals
    FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
    HTHG = Half Time Home Team Goals
    HTAG = Half Time Away Team Goals
    HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

    HS = Home Team Shots
    AS = Away Team Shots
    HST = Home Team Shots on Target
    AST = Away Team Shots on Target

    HY = Home Team Yellow Cards
    AY = Away Team Yellow Cards
    HR = Home Team Red Cards
    AR = Away Team Red Cards

'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Load training files
train_epl00 = pd.read_csv('./data/EPL00_01.csv', encoding="ISO-8859-1")
train_epl01 = pd.read_csv('./data/EPL01_02.csv', encoding="ISO-8859-1")
train_epl02 = pd.read_csv('./data/EPL02_03.csv', encoding="ISO-8859-1")

# Load testing files
test_epl03 = pd.read_csv('./data/EPL03_04.csv', encoding="ISO-8859-1")
test_epl04 = pd.read_csv('./data/EPL04_05.csv', encoding="ISO-8859-1")

# Concat all training files into one structure
df_train = pd.concat((train_epl00, train_epl01, train_epl02), axis=0, ignore_index=True)
df_test  = pd.concat((test_epl03, test_epl04), axis=0, ignore_index=True)

# Number of records in training set
num_train = df_train.shape[0]
print(str(num_train) + " rows read from multiple training files.")

# Number of records in test set
num_test = df_test.shape[0]
print(str(num_test) + " rows read from multiple test files.")

# As a test, plot the away shots to home shots
plt.scatter(df_train['HS'], df_train['AS'], marker='o', edgecolor='b', facecolor='none', alpha=0.5)
plt.xlabel('Home Shots')
plt.ylabel('Away Shots')
plt.savefig('hometoawaygoals.png', fmt='png', dpi=100)
