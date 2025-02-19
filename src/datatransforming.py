from .datacleaning import datacleaning
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib as j
obj = datacleaning()
df = obj.clean_data()
class datatransform:
    def __init__(self):
        pass
    def transform_data(self):
        x=df.drop("Survived",axis=1)
        y=df["Survived"]
        cat=x.select_dtypes(object).columns
        num=x.select_dtypes(int).columns
        
        scaler = StandardScaler()
        scaler.fit(x[num])
        j.dump(scaler, "models/scaler.pkl")
        x[num] = scaler.transform(x[num])
        encoder = LabelEncoder()
        for col in cat:
            encoder.fit(x[col])
            j.dump(encoder, "models/encoder.pkl") 
            x[col] = encoder.transform(x[col])


        
        return x,y