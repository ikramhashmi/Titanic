from src.datasplitting import data_splitting
from pipelines.model import Model
import joblib as j
split = data_splitting()
model = Model()
x_train, x_test, y_train, y_test =split.splitter()
log_reg=model.datamodel()
print("Starting Training")
model = log_reg.fit(x_train, y_train)
j.dump(model, 'models/model.pkl')
print('Model saved')



