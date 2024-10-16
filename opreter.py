import pandas as pd
data={
    'Title':['Book1','Book2',"Book3","Book4"],
    'Publication_Years':[1995,1996,1997,1998],
    'Price':[10,20,30,100],
    'Author':['Jane Austen', 'F. Scott Fitzgerald','saroj','Jane Austen']
}
book_df=pd.DataFrame(data)
# print(book_df['Publication_Years'],book_df['Publication_Years']==1996,sep=",",end="")
# recent_and_cheap_book=book_df[(book_df['Publication_Years']>1995) & (book_df['Publication_Years']<1996) ]
# print(recent_and_cheap_book)

#  and operator

recent_and_cheap_book=book_df[(book_df['Author']=="Jane Austen") & (book_df['Price']==10) 
]
# print(recent_and_cheap_book)


# or operators


recent_and_cheaps_book=book_df[(book_df['Publication_Years']>1950) | (book_df['Price']<10)]
# print(recent_and_cheaps_book)
year=1997
old_books = book_df[~(book_df['Publication_Years'] > year)]
# print(old_books)
old_books = book_df[(book_df['Publication_Years'] > year)]
# print(old_books)



# logical operator

filtered_books = book_df[((book_df['Publication_Years'] > 1950) & (book_df['Price'] < 10)) | (book_df['Author'] == 'Jane Austen')]
print(filtered_books)