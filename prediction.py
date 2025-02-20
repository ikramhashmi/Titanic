import joblib as j
import pandas as pd

sc=j.load("models/scaler.pkl")
en=j.load("models/encoder.pkl")
model = j.load("models/model.pkl")



def prediction(data, scaler=sc, encoder=en, model=model):
    categorical_cols = select_dtypes(include=['object']).columns.tolist()
    numerical_cols = select_dtypes(include=['number']).columns.tolist()

    data[categorical_cols] = encoder.transform(data[categorical_cols])
    data[numerical_cols] = scaler.transform(data[numerical_cols])
    prediction = model.predict(data)
    return prediction
    
print(prediction(data))