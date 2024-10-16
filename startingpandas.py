# Getting starting pandas


import pandas as pd
# print(pd)
data={'name':['Alice','Bob','Charlie','David'],
      'age':[35,43,10,30],
      'city':['New york','india','chicago','Houston']}
df=pd.DataFrame(data)
print(df)
