# Pandas Merging dataframes

Merging dataframes in pandas is a powerfull way to combine data from multiple sources into a single dataframe.

Pandas provide several methods to achive this, but the most common method one is `merge()` function.

`Syntax:`

```py
pd.merge(left,right, how='left|right|inner|outer',left_on='',right_on='',left_index='',right_index='')
```

`Note:`

- `left:` The first dataframe.
- `right:` The second dataframe.
- `how:` The type of join to perform. Options include 'left', 'right', 'outer', and 'inner'.
- `on:` Column or index level name(s) to join on. Must be found in both dataframes.
- `left_on:` Column or index level name(s) in the left dataframe to join on.
- `right_on:` Column or index level name(s) in the right dataframe to join on.
- `left_index:` If True, use the index from the left dataframe as the join key(s).
- `right_index:` If True, use the index from the right dataframe as the join key(s).

`Example:`

```py
import numpy as np
import pandas as pd


food = pd.read_csv("csv/restaurant_foods.csv")
customers = pd.read_csv("csv/restaurant_customers.csv")
week_1 = pd.read_csv("csv/restaurant_week_1_sales.csv")
week_2 = pd.read_csv("csv/restaurant_week_2_sales.csv")

print(week_1.head())
print(food.head())

df = pd.merge(food, week_1, how="left", on="Food ID")

print(df)
```

<br />

**`Types of Joins:`**

- `Inner Join:`
  Returns only the rows with matching keys in both dataframes.

  `Syntax:`

  ```py
  pd.merge(df1, df2, how='inner', on='key')
  ```

  `Example:`

  ```py
    import pandas as pd

    df1 = pd.DataFrame({
        'key': ['A', 'B', 'C'],
        'value1': [1, 2, 3]
    })

    df2 = pd.DataFrame({
        'key': ['B', 'C', 'D'],
        'value2': [4, 5, 6]
    })

    # To merge these dataframes on the 'key' column with an inner join:
    result = pd.merge(df1, df2, how='inner', on='key')

    # The resulting dataframe result will look like this:
        key  value1  value2
    0   B       2       4
    1   C       3       5
  ```

- `Left Join:`
  Returns all rows from the left dataframe, and the matched rows from the right dataframe. Unmatched rows will have NaN in the right dataframe’s columns.

  `Syntax:`

  ```py
  pd.merge(df1, df2, how='left', on='key')
  ```

  `Example:`

  ```py
    import pandas as pd

    # To merge these dataframes on the 'key' column with an left join:
    result = pd.merge(df1, df2, how='left', on='key')

    # The resulting dataframe result will look like this:
        key  value1  value2
    0   A       1     NaN
    1   B       2     4.0
    2   C       3     5.0
  ```

- `Right Join:`
  Returns all rows from the right dataframe, and the matched rows from the left dataframe. Unmatched rows will have NaN in the left dataframe’s columns.

  `Syntax:`

  ```py
  pd.merge(df1, df2, how='right', on='key')
  ```

  `Example:`

  ```py
    import pandas as pd

    # To merge these dataframes on the 'key' column with an right join:
    result = pd.merge(df1, df2, how='right', on='key')

    # The resulting dataframe result will look like this:
        key  value1  value2
    0   B     2.0       4
    1   C     3.0       5
    2   D     NaN       6
  ```

- `Outer Join:`
  Returns all rows from both dataframes. Unmatched rows will have NaN in the columns from the dataframe where there is no match.

  `Syntax:`

  ```py
  pd.merge(df1, df2, how='outer', on='key')
  ```

  `Example:`

  ```py
    import pandas as pd

    # To merge these dataframes on the 'key' column with an right join:
    result = pd.merge(df1, df2, how='right', on='key')

    # The resulting dataframe result will look like this:
        key  value1  value2
    0   A     1.0     NaN
    1   B     2.0     4.0
    2   C     3.0     5.0
    3   D     NaN     6.0
  ```

`Examples:`

- `Merge on multple columns:`

  ```py
  df1 = pd.DataFrame({
      'key1': ['A', 'B', 'C'],
      'key2': ['X', 'Y', 'Z'],
      'value1': [1, 2, 3]
  })

  df2 = pd.DataFrame({
      'key1': ['B', 'C', 'D'],
      'key2': ['Y', 'Z', 'W'],
      'value2': [4, 5, 6]
  })

  result = pd.merge(df1, df2, how='inner', on=['key1', 'key2'])
  ```

- `Merge on index:`

  ```py
  df1 = pd.DataFrame({
      'value1': [1, 2, 3]
  }, index=['A', 'B', 'C'])

  df2 = pd.DataFrame({
      'value2': [4, 5, 6]
  }, index=['B', 'C', 'D'])

  result = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
  ```
