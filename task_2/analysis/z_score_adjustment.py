import numpy as np


def adjust_for_outliers(department_means, threshold=3):
    """
    Adjust department mean scores based on Z-score to handle outliers.

    Parameters:
        department_means (list of float): Mean threat scores for each department.
        threshold (int): Z-score threshold to cap outliers.

    Returns:
        list of float: Adjusted department mean scores.

    Explanation:
        Z-score is a measure of how far a value is from the mean, in terms of standard deviations.
        If Z-score is greater or less than threshold it is misrepresenting outlier of the analysis.
        From mean - (threshold * std_dev) to mean + (threshold * std_dev) is the range for means
        to capp the outliers
    """
    mean = np.mean(department_means)
    std_dev = np.std(department_means)
    z_scores = [(x - mean) / std_dev for x in department_means]

    adjusted_means = []
    for i, z in enumerate(z_scores):
        if abs(z) > threshold:
            if z > 0:
                adjusted_value = mean + (threshold * std_dev)
            else:
                adjusted_value = mean - (threshold * std_dev)
            adjusted_means.append(adjusted_value)
        else:
            adjusted_means.append(department_means[i])

    return adjusted_means
