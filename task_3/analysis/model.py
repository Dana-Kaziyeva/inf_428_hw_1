from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def build_and_train_model(df):
    """
    Build and train a simple regression model to predict time differences.
    :param df: DataFrame containing features and the target (time difference).
    :return: Trained model
    """
    # Features (hour, minute, second for both timestamps)
    X = df[['hour_1', 'minute_1', 'second_1', 'hour_2', 'minute_2', 'second_2']]

    # Target (time difference in seconds)
    y = df['time_diff_sec']


    X_train, y_train = X, y
    X_test, y_test = X, y

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the time difference on test data
    y_pred = model.predict(X_test)

    # Calculate Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    return model
