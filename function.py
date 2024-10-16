import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 15, 30, 10, 25],
    'Quantity': [1, 2, 3, 4, 2, 3]
}
df=pd.DataFrame(data)
# print(df)

# 4. Aggregating with Custom Functions..........

# Custom aggregation function: Range (max - min)

def range_func(x):
    return x.max() - x.min()
custom_aggregation = df.groupby('Category')['Values'].agg(range_func)
# print(custom_aggregation)


#5. Handling Missing Data in Aggregations....................
# Adding missing values to the DataFrame...

df_with_nan = df.copy()
df_with_nan.loc[2, 'Values'] = None


# Group by 'Category' and calculate the sum, skipping NaN values

grouped_sum_with_nan = df_with_nan.groupby('Category')['Values'].sum()
print(grouped_sum_with_nan)


# Fill missing values before aggregation
filled_df = df_with_nan.fillna(0)
grouped_sum_filled = filled_df.groupby('Category')['Values'].sum()
# print( grouped_sum_filled)


