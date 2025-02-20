from src.datasplitting import data_splitting
from pipelines.model import Model
from sklearn.metrics import accuracy_score
import joblib as j
split = data_splitting()
model = Model()
x_train, x_test, y_train, y_test =split.splitter()
grid_search=model.datamodel()
print("Starting Training")
grid_search.fit(x_train, y_train)
print("Training Done")
y_pred = grid_search.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
model = grid_search.best_estimator_
j.dump(model, "models/model.pkl")
print("Model Saved")



