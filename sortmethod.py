import pandas as pd
data={
    'Title':['Book1','Book2',"Book3","Book4"],
    'Publication_Years':[1995,1996,1997,1998],
    'Price':[10,20,10,100],
    'Author':['Jane Austen', 'F. Scott Fitzgerald','saroj','Jane Austen']
}
book_df=pd.DataFrame(data)

#  ascending order......................

book_sorted_by_years=book_df.sort_values(by='Publication_Years')
# print(book_sorted_by_years)

#  descending order......................

books_sorted_by_price = book_df.sort_values(by='Price', ascending=False)
# print(books_sorted_by_price)


# 2. `sort_index()` Method..................

sorted_by_index = book_df.sort_index(axis=0)
# print(sorted_by_index)
sorted_by_index = book_df.sort_index(axis=1)
# print(sorted_by_index)



# nlargest() and nsmallest() Methods............


top_expensive_books = book_df.nlargest(2, 'Price')
# print(top_expensive_books)

oldest_books = book_df.nsmallest(2, 'Publication_Years')
# print(oldest_books)

# rank() Method..........................


# (e.g., 'average', 'min', 'max', 'first', 'dense')

book_df['Price_Rank'] = book_df['Price'].rank(method='first')
print(book_df['Price_Rank'])






