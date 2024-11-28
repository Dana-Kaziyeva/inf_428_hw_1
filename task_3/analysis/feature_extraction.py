import pandas as pd


def extract_time_features(df):
    """
    Extract hour, minute, second features from the timestamps and calculate their difference in hours, minutes, and seconds.

    :param df: DataFrame containing 'timestamp_1' and 'timestamp_2' columns.
    :return: DataFrame with extracted features and the time difference in hours, minutes, and seconds.
    """
    # Convert timestamps to datetime format
    try:
        df['timestamp_1'] = pd.to_datetime(df['timestamp_1'])
        df['timestamp_2'] = pd.to_datetime(df['timestamp_2'])
    except Exception as e:
        print(f"Error converting timestamps: {e}")
        return df  # Return the df as-is in case of error for debugging

    # Extract hour, minute, second from each timestamp
    df['hour_1'] = df['timestamp_1'].dt.hour
    df['minute_1'] = df['timestamp_1'].dt.minute
    df['second_1'] = df['timestamp_1'].dt.second

    df['hour_2'] = df['timestamp_2'].dt.hour
    df['minute_2'] = df['timestamp_2'].dt.minute
    df['second_2'] = df['timestamp_2'].dt.second

    # Calculate time difference in seconds
    df['time_diff_sec'] = (df['timestamp_2'] - df['timestamp_1']).dt.total_seconds()
    # If the time difference is negative, add 24 hours (in seconds) to make it positive
    df['time_diff_sec'] = df['time_diff_sec'].apply(lambda x: x + 86400 if x < 0 else x)
    # Convert the difference into hours, minutes, and seconds
    df['diff_hours'] = df['time_diff_sec'] // 3600
    df['diff_minutes'] = (df['time_diff_sec'] % 3600) // 60
    df['diff_seconds'] = df['time_diff_sec'] % 60

    # Return the DataFrame with relevant features
    return df[['hour_1', 'minute_1', 'second_1', 'hour_2', 'minute_2', 'second_2', 'diff_hours', 'diff_minutes', 'diff_seconds','time_diff_sec']]
