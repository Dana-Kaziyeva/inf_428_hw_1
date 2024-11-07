import pandas as pd


def extract_time_features(df):
    """
    Extract useful time-related features such as hour, minute, and day of the week
    from a 'timestamp' column in the DataFrame.

    :param df: DataFrame with a 'timestamp' column.
    :return: DataFrame with additional time-based features.
    """
    df['hour'] = df['timestamp'].dt.hour
    df['minute'] = df['timestamp'].dt.minute
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    return df
