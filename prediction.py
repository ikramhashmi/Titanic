import joblib as j
import pandas as pd
sc=j.load("models\\scaler.pkl")
model = j.load("models\\model.pkl")


df=pd.read_csv("artifacts\\cleaned.csv")
# data=df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
data=df.head(1).values

def prediction(data=data,sc=sc,model=model):
    # data=sc.transform(data)
    prediction=model.predict(data)
    return prediction

print(prediction)
    