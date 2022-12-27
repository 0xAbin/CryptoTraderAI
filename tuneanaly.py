#  GridSearchCV from scikit-learn
from sklearn.model_selection import GridSearchCV

#  hyperparameter grid
param_grid = {'param1': [1, 2, 3],
              'param2': [4, 5, 6]}

# grid search object
grid_search = GridSearchCV(model, param_grid, cv=5)

# fit the grid search object to the training data
grid_search.fit(X_train, y_train)

# the best parameters
print(grid_search.best_params_)

# update the model with the best parameters
model = grid_search.best_estimator_





