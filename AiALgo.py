# algorithms
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# choose the algorithm (stage 0.1)
if task == 'predict_price':
    model = LinearRegression()
elif task == 'identify_patterns':
    model = DecisionTreeRegressor()
else:
    model = SVR()

