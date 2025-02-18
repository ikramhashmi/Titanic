from .dataloading import dataloader
obj = dataloader()
PATH= r"artifacts\tested.csv"
df = obj.load_data(PATH)
class datacleaning:
    def __init__(self):
        pass
    def clean_data(self,df = df):
        df.drop(["PassengerId","Name","Ticket","Cabin"],inplace=True,axis=1)
        df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
        df['Fare']=df['Fare'].fillna(df['Fare'].median())
        return df     