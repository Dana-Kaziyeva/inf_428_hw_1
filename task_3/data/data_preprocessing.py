
def normalize_data(df):
    """
    Normalize numerical columns in the DataFrame.

    :param df: DataFrame to normalize.
    :return: Normalized DataFrame.
    """
    return (df - df.min()) / (df.max() - df.min())
