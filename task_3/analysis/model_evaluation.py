from sklearn.metrics import mean_squared_error


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model performance using Mean Squared Error (MSE).

    :param model: The trained machine learning model.
    :param X_test: Test features (input data).
    :param y_test: Test labels (true values).
    :return: Mean Squared Error of the model predictions.
    """
    predictions = model.predict(X_test)
    return mean_squared_error(y_test, predictions)
