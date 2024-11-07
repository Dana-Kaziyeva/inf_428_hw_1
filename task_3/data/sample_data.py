import pandas as pd


def generate_sample_data():
    """
    Generate a small sample DataFrame with a 'timestamp' column.

    :return: DataFrame with sample timestamps and values.
    """
    return pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-11-08 09:00:00', '2024-11-08 18:30:00']),
        'value': [10, 20]
    })
