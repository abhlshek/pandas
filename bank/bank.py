import pandas as pd

# df=pd.read_excel("bank/Book1.xlsx")


def readfromexcel():
    df=pd.read_excel("bank/Book1.xlsx",index_col=0)
    return df


def getaccountno(accountno):
    try:
        df=readfromexcel()
        account = df[df['accountno'] == accountno]
        return account
    except:
        return None


x=getaccountno(100)
print(x)





def SaveToExcel(df):
    df.to_excel("bank/Book1.xlsx")







def NewAccount(accountno,name,balance):
    try:
        newdata = {

                   'balance': balance,
                   "name": name
                   }
        df = readfromexcel()
        print(newdata)
        df.loc[accountno]=newdata
        print('df',df)
        SaveToExcel(df)
        return True
    except:
        return False
    

# x=NewAccount(31,'sandeep',200)
# print(x)


def ChangeBalance(accountno,newbalance):
    try:
        newdata = {'accountno': [accountno],

               'balance': [newbalance]
               }
        newdata = pd.DataFrame(newdata, index=newdata["accountno"])
        print(newdata)
        df=readfromexcel()
        df.update(newdata)

        SaveToExcel(df)
        return True
    except:
        return False
# x=ChangeBalance(31,100)
# print(x)

def CloseAccount(accountno):
    try:
        df = readfromexcel()
        df=df.drop(accountno)
        print(df)
        SaveToExcel(df)
        return True
    except:
        return False
    
x=CloseAccount(31)
print(x)


