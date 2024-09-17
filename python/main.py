import numpy as np
import pandas as pd


food = pd.read_csv("csv/restaurant_foods.csv")
customers = pd.read_csv("csv/restaurant_customers.csv")
week_1 = pd.read_csv("csv/restaurant_week_1_sales.csv")
week_2 = pd.read_csv("csv/restaurant_week_2_sales.csv")

print(week_1.head())
print(food.head())

df = pd.merge(food, week_1, how="left", on="Food ID")

# print(df)


df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

# To merge these dataframes on the 'key' column with an inner join:
result = pd.merge(df1, df2, how='outer', on='key')

print(result)
