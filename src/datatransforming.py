from .datacleaning import datacleaning
import pandas as pd
from sklearn.preprocessing import StandardScaler
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
        x[num] = scaler.fit_transform(x[num])
        x_categorical_encoded = pd.get_dummies(x[cat], drop_first=False)
        x = pd.concat([x[num], x_categorical_encoded], axis=1)
        return x,y