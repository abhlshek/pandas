import pandas as pd


data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Amit', 'Priya', 'Vikram', 'Anjali', 'Rahul', 'Neha'],
    'age': [24, 27, 22, 32, 29, 35],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Kolkata'],
    'score': [88, 92, 85, 70, 90, 95]
}

df =pd.DataFrame(data)
# print(df)


# 2. Using `query` Method;

#Example:Select names and scores for people who scored more than 85.

result=df[df['score']>85]
# print(result)

# 3. `loc` and `iloc`;
  # 1. `loc`: Label-based indexing to select specific rows and columns.
  #2.`iloc`:** Integer-based indexing to select specific rows and columns.
  
# Example: Select rows with index labels 1 and 3 and columns 'name' and 'score'.
# print(df)

result=df.loc[[1,3],['name','score']]
# print(result)
result=df.iloc[[1,3],[1,4]]
# print(result)


#4. Combining Multiple Conditions

result = df[(df['age'] > 25) & (df['score'] < 90)]


# print(result)


#5. Using String Functions

# Example:** Select rows where the name contains the letter 'a'.


result=df[df['name'].str.contains('M',case=False)]
# print(result)

#6. Using `isin` Method

# Example:Select rows where the city is either 'Bangalore' or 'Chennai'.

result = df[df['city'].isin(['Bangalore', 'Chennai'])]
# print(result)

#7. Sorting

# Example:** Select all rows and sort by score in descending order.

result = df.sort_values(by='score', ascending=False)
# print(result)


#8. Aggregations
# Example:** Calculate the average score of all individuals.

average_score = df['score'].mean()
# print(average_score)


### 9. Grouping
# Example:** Group by 'city' and calculate the mean age for each city.

result = df.groupby('city')['age'].mean()
print(result)

# 10. Selecting Top N Rows
# **Example:** Select the top 3 rows with the highest scores.

result = df.nlargest(3, 'score')
print(result)





















