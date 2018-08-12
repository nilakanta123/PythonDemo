import pandas as pd
import numpy as np

# @@@@@@@@ READING DATA @@@@@@@
df = pd.read_csv('sample.csv')
print("\n------ PRINTING DATAFRAME -------------\n")
print(df)
print("\n------ PRINTING COLUMN -------------\n")
print(df.columns)
print("\n------ PRINTING FULL DATA -------------\n")
print(df.values)
print("\n------ DROPPING COLUMN -------------\n")
df.drop(['col2'], axis=1, inplace=True)
print(df)
print("\n => To select rows whose column value equals a scalar, some_value, use ==:\n")
print(df.loc[df['col4'] == 483])
print("\n => Combine multiple conditions with &:")
l = [8.69,195.99]
print(df.loc[(df['col3'] == "Barry French") & df['col6'].isin(l)])
print("\n => To select rows whose column value does not equal some_value, use !=: \n")
print(df.loc[df['col3'] != "Carlos Soltero"])
print("\n => To select rows whose value is not in some_values, negate the boolean Series using ~: \n")
ll=["Carl Jackson","Barry French"]
print(df.loc[~df['col3'].isin(ll)])