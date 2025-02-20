from .dataloading import dataloader
import pandas as pd
obj = dataloader()
PATH= "artifacts\\merged_titanic.csv"
df = obj.load_data(PATH)
class datacleaning:
    def __init__(self):
        pass
    def clean_data(self,df = df):
        df.drop(["PassengerId","Name","Ticket","Cabin"],inplace=True,axis=1)
        df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
        df['Fare']=df['Fare'].fillna(df['Fare'].median()).astype(int)
        df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
        df.dropna(subset=['Survived'], inplace=True)
        df['Survived']=df['Survived'].astype(int)
        df.to_csv("artifacts\\cleaned.csv",index=False)
        return df  
   