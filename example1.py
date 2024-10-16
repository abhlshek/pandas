import pandas as pd

data={
    'id':[1,2,3,4,5,6],
    'name': ['Amit', 'Priya', 'Vikram', 'Anjali', 'Rahul', 'Neha'],
    'age': [24, 27, 22, 32, 29, 35],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Kolkata'],
    'score': [88, 92, 85, 70, 90, 95]
}

# 1.Select all rows where age is greater than 25:

df=pd.DataFrame(data)
# print(df)
result=df[df['age']>25]
# print(result)

# 2.Select names and scores for people who scored more than 85:

result=df.query('score>85')[['name','score']]
# print(result)

# 3.Select rows where the city is either 'Bangalore' or 'Chennai':


result=df[df['city'].isin(['Bangalore','Chennai'])]
# print(result)

# 4. Select all rows and sort by score in descending order:


result=df.sort_values(by='score',ascending=True)
# print(result)

# 5. Calculate the average score of all individuals:
average_score=df['score'].mean()
# print(average_score)

# 6.Group by 'city' and calculate the mean age for each city:
result=df.groupby('city')['age'].mean()
# print(result)


# 7. Filter rows where the name contains the letter 'a':
result=df[df['name'].str.contains('a',case=False)]
# print(result)

# 8. Select the top 3 rows with the highest scores:
result=df.nlargest(3,'score')
print(result)








