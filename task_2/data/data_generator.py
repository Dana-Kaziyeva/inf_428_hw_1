import numpy as np


def generate_random_data(mean, variance, num_samples):
    """
    Generate random threat scores for a department using mean, variance and num_samples.

    Parameters:
        mean (int): The mean threat score of the department.
        variance (int): The variance around the mean of the department.
        num_samples (int): Number of samples (users) in the department.

    Returns:
        np.array: Array of random threat scores within the range [0, 90].

    Explanation:
        np.random.randint() generates values within a set range from mean - variance
        (it takes 0 instead if the subtraction is negative value) to mean + variance + 1
        (it takes 90 if mean + variance + 1 is more than 90;  + 1 to ensure mean + variance
        is included, because .random.randint() is exclusive of its upper limit)
    """
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)
