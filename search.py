import pandas as pd
data={
    'Title':['Book1','Book2',"Book3","Book4"],
    'Publication_Years':[1995,1996,1997,1998]
}
book_df= pd.DataFrame(data)
# print(book_df)
recent_book=book_df[book_df['Publication_Years']>=1996]
# print(recent_book)

chip_recent_book= book_df[(['Publication_Years']>1995)&(book_df['price']) <10]
print(chip_recent_book)
