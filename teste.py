import pandas as pd

df = pd.read_csv("usuarios.csv")

df.loc[df["codigo"] == 12399] = ['a','b', 'c', 'd', 'c']

print(df)