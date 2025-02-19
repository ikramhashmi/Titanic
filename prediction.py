import joblib as j
import pandas as pd

sc=j.load("models/scaler.pkl")
en=j.load("models/encoder.pkl")
model = j.load("models/model.pkl")
def clean_data(df):
    
    df = df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
    if df.isnull().any().any():
        raise ValueError("Missing values found. Please provide all required fields.")
    return df
def prediction(data, scaler=sc, encoder=en, model=model):
    data = clean_data(data)
    categorical_cols = ['Sex', 'Embarked']  
    numerical_cols = ['Age', 'Fare', 'Pclass', 'SibSp', 'Parch']
    data[categorical_cols] = encoder.transform(data[categorical_cols])
    data[numerical_cols] = scaler.transform(data[numerical_cols])
    prediction = model.predict(data)
    return prediction
    
print(prediction())