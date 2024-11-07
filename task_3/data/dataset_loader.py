import pandas as pd


def load_dataset(filepath):
    """
    Load a dataset from a CSV file.

    :param filepath: Path to the CSV file.
    :return: DataFrame loaded from the CSV file.
    """
    return pd.read_csv(filepath)
