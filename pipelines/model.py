from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
class Model:
    def __init__(self):
        pass
    def  datamodel(self):
        param_grid = {
    'C': [10, 50, 100],  
    'gamma': [0.01, 0.05, 0.1],  
    'kernel': ['rbf'],  
}
        svm_model = SVC()
        grid_search = GridSearchCV(svm_model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
        return grid_search