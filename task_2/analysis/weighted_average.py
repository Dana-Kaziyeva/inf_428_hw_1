import numpy as np


def calculate_weighted_average(departments_mean):
    """
    Compute the average of department mean threat scores.

    Parameters:
        departments_mean (list of float): Mean scores for each department.

    Returns:
        float: Average of department mean scores.
    """
    return sum(departments_mean) / len(departments_mean)
