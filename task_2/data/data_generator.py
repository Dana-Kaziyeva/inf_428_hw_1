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
    lower_bound = max(mean - variance, 0)
    upper_bound = min(mean + variance + 1, 90)

    # Ensure lower bound is less than upper bound
    if lower_bound >= upper_bound:
        lower_bound = max(upper_bound - 1, 0)

    return np.random.randint(lower_bound, upper_bound, num_samples)
