import pandas as pd
class dataloader:
    def __init__(self):
        pass
    def load_data(self,path):
        df=pd.read_csv(path)
        retrun df