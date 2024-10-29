import pandas as pd
def readfromexcel():
    df=pd.read_excel("bank/sbi.xlsx",index_col=0)
    return df


def GetBalance(accno):
    try:
        df=readfromexcel()
        x = df[['balance']]

        return x.loc[accno][0]

    except:
        return None
def CloseAccount(accno):
    try:
        df = readfromexcel()
        df=df.drop(accno)
        print(df)
        SaveToExcel(df)
        return True
    except:
        return False
def NewAccount(accno,name,balance):
    try:
        newdata = {

                   'balance': balance,
                   "name": name
                   }
        df = readfromexcel()
        print(newdata)
        df.loc[accno]=newdata
        print('df',df)
        SaveToExcel(df)
        return True
    except:
        return False
    
def ChangeBalance(accno,newbalance):
    try:
        newdata = {'accno': [accno],

               'balance': [newbalance]
               }
        newdata = pd.DataFrame(newdata, index=newdata["accno"])
        print(newdata)
        df=readfromexcel()
        df.update(newdata)

        SaveToExcel(df)
        return True
    except:
        return False
def SaveToExcel(df):
    df.to_excel("bank/sbi.xlsx")
# NewAccount(44,"Jetha",500)
# CloseAccount(44)
balance=GetBalance(4)
print(balance)
# ChangeBalance(4,400)
# x=GetBalance(3)
# print(x)
"""

x=GetBalance(3)
print(x)
x=NewAccount(4,"Champak",300)
print(x)
"""