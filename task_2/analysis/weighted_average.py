import numpy as np


def calculate_weighted_average(departments_mean, importance_weights):
    """
    Compute the overall weighted average threat score for the company.

    Parameters:
        departments_data (list of np.array): List of threat scores for each department.
        importance_weights (list of int): Importance tag for each department.

    Returns:
        float: Weighted average of department mean scores.
    """
    total_weighted_score = 0  #sum of the weighted mean scores of all departments
    total_weight = 0          #sum of all the importance tags

    for i, department_mean in enumerate(departments_mean):
        total_weighted_score += department_mean * importance_weights[i]
        total_weight += importance_weights[i]

    aggregated_score = total_weighted_score / total_weight
    return aggregated_score
