import numpy as np

from z_score_adjustment import adjust_for_outliers


def compute_aggregated_threat_score(departments_data, importance_weights, z_threshold=3):
    """
    Computes the final aggregated threat score using weighted average and outlier adjustment.

    Parameters:
        departments_data (list of np.array): List of threat scores for each department.
        importance_weights (list of int): Importance weights for each department.
        z_threshold (int): Z-score threshold for adjusting outliers.

    Returns:
        float: Final aggregated threat score within the range [0, 90].
    """
    department_means = [np.mean(dept) for dept in departments_data]
    adjusted_means = adjust_for_outliers(department_means, threshold=z_threshold)

    total_weighted_score = sum(adjusted_mean * importance_weights[i] for i, adjusted_mean in enumerate(adjusted_means))
    total_weight = sum(importance_weights)

    return total_weighted_score / total_weight
