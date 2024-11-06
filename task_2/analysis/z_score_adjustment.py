import numpy as np


def adjust_for_outliers(department_means, threshold=3):
    """
    Adjusts department mean scores based on Z-score to handle outliers.

    Parameters:
        department_means (list of float): Mean threat scores for each department.
        threshold (int): Z-score threshold to cap outliers.

    Returns:
        list of float: Adjusted department mean scores.
    """
    mean = np.mean(department_means)
    std_dev = np.std(department_means)
    z_scores = [(x - mean) / std_dev for x in department_means]

    adjusted_means = []
    for i, z in enumerate(z_scores):
        if abs(z) > threshold:
            adjusted_value = mean + (threshold * std_dev if z > 0 else -threshold * std_dev)
            adjusted_means.append(adjusted_value)
        else:
            adjusted_means.append(department_means[i])

    return adjusted_means
