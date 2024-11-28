import numpy as np

from analysis.z_score_adjustment import adjust_for_outliers
from analysis.weighted_average import calculate_weighted_average

def compute_aggregated_threat_score(departments_data, z_threshold=3):
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

    return calculate_weighted_average(adjusted_means)
