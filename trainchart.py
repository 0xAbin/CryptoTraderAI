# train_test_split from scikit-learn
from sklearn.model_selection import train_test_split

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# fit the model to the training data
model.fit(X_train, y_train)


