from sklearn.linear_model import LogisticRegression
class Model:
    def __init__(self):
        pass
    def  datamodel(self):
        log_reg = LogisticRegression(max_iter=1000, random_state=42)   
        return log_reg