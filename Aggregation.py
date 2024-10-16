import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 15, 30, 10, 25],
    'Quantity': [1, 2, 3, 4, 2, 3]
}
df=pd.DataFrame(data)
print(df)

# 1.Basic Aggregation Functions........................

# sum..........

total_value=df['Values'].sum()
# print(total_value)
total_quantity=df['Quantity'].sum()
# print(total_quantity)

# mean.........
total_value=df['Values'].mean()
# print(total_value)

# max.........
total_value=df['Values'].max()
# print(total_value)

# min.........

total_value=df['Values'].min()
# print(total_value)

# count......

total_value=df['Values'].count()
# print(total_value)





#2. Grouping data.....
grouped_sum = df.groupby('Category')['Values'].sum()
# print(grouped_sum)

grouped_mean = df.groupby('Category')['Values'].mean()
# print(grouped_mean)

grouped_max = df.groupby('Category')['Values'].max()
# print(grouped_max)

grouped_min = df.groupby('Category')['Values'].min()
# print(grouped_min)


# 3. Applying Multiple Aggregations..............

multiple_aggregations = df.groupby('Category')['Values'].agg(['sum', 'mean', 'max', 'min'])
# print(multiple_aggregations)












