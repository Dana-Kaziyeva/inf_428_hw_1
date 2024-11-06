import numpy as np


def generate_random_data(mean, variance, num_samples):
    """
    Generates random threat scores for a department.

    Parameters:
        mean (int): The mean threat score.
        variance (int): The variance around the mean.
        num_samples (int): Number of samples (users) in the department.

    Returns:
        np.array: Array of random threat scores within the range [0, 90].
    """
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)
