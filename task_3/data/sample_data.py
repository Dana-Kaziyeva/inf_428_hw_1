import pandas as pd
import numpy as np

def generate_sample_data():
    """
    Generate a DataFrame with two random timestamps and corresponding values.
    The timestamps are randomly generated with only hours, minutes, and seconds.

    :return: DataFrame with random timestamps (hours, minutes, seconds) and values.
    """
    # Generate two random times, without year, month, day (just hour, minute, second)
    times = pd.to_datetime(
        np.random.choice(pd.date_range('2024-01-01 00:00:00', '2024-01-01 23:59:59', freq='s'), size=2))

    # Extract hour, minute, second from the generated timestamps
    time_data = {
        'timestamp_1': times[0].strftime('%H:%M:%S'),
        'timestamp_2': times[1].strftime('%H:%M:%S'),
    }

    # Create DataFrame
    df = pd.DataFrame([time_data])
    return df


