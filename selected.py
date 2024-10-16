import pandas as pd
data={
    'Title':['Book1','Book2',"Book3","Book4"],
    'Publication_Years':[1995,1996,1997,1998],
    'Price':[10,20,30,100],
    'Author':['Jane Austen', 'F. Scott Fitzgerald','saroj','rahul']
}
book_df=pd.DataFrame(data)
selected_authors=['Jane Austen', 'F. Scott Fitzgerald']
selected_book=book_df[book_df['Author'].isin(selected_authors)]
print(selected_book)