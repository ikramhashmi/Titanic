from sklearn.model_selection import train_test_split
from .datatransforming import datatransform
obj = datatransform()
x,y = obj.transform_data()
class data_splitting:
    def __init__(self):
        pass
    def splitter(self):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        return x_train, x_test, y_train, y_test 