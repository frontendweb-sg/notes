import pandas as pd
import numpy as np

a = list((1, 2, 3, 4, 5))
i = list("abcde")
s = pd.Series(a, index=i)
print(s)
