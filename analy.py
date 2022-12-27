#  predictions on the testing data
y_pred = model.predict(X_test)

# calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# calculate the root mean squared error
rmse = np.sqrt(mse)

print("Root Mean Squared Error:", rmse)




