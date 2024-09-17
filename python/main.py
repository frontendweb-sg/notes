import pandas as pd
from pydataset import data
import matplotlib.pyplot as plt


l = list(('A', 'B', 'C', 'D', 'E'))
s = pd.Series(l)

# Data Frame

df1 = pd.DataFrame(s, columns=['A'])
df2 = pd.DataFrame(s, columns=['B'])


df = pd.concat((df1, df2), ignore_index=True)
df = pd.concat((df1, df2)).sort_index()
df = pd.concat((df1, df2), keys=['Alpha 1', 'Alpha 2'])

df = pd.concat((df1, df2), axis="columns")

print(df)
