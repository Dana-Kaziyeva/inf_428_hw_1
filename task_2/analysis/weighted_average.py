import numpy as np


def calculate_weighted_average(departments_data, importance_weights):
    """
    Computes the weighted average of department mean threat scores.

    Parameters:
        departments_data (list of np.array): List of threat scores for each department.
        importance_weights (list of int): Importance weights for each department.

    Returns:
        float: Weighted average of department mean scores.
    """
    total_weighted_score = 0
    total_weight = 0

    for i, department in enumerate(departments_data):
        department_mean = np.mean(department)
        total_weighted_score += department_mean * importance_weights[i]
        total_weight += importance_weights[i]

    aggregated_score = total_weighted_score / total_weight
    return aggregated_score
