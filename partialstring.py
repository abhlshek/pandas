import pandas as pd
data={
    'Title':['Book1 is great','Book2',"Book3","Book4"],
    'Publication_Years':[1995,1996,1997,1998],
    'Price':[10,20,30,100]
}
book_df= pd.DataFrame(data)
great_book=book_df[book_df['Title'].str.contains('great')]
print(great_book)