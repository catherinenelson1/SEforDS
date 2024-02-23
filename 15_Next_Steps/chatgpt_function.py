from typing import List


def weighted_mean(numbers: List[float], weights: List[float]) -> float:
    """
    Calculate the weighted mean of a list of numbers.

    Parameters:
    - numbers (List[float]): List of numbers.
    - weights (List[float]): List of weights (same length as numbers).

    Returns:
    - float: Weighted mean of the numbers.

    Raises:
    - ValueError: If the lengths of numbers and weights do not match,
                  or if any weight is zero.

    Example:
    >>> numbers = [10, 20, 30, 40, 50]
    >>> weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    >>> weighted_mean(numbers, weights)
    30.0
    """
    if len(numbers) != len(weights):
        raise ValueError("The number of numbers and weights must be the same.")

    if any(w == 0 for w in weights):
        raise ValueError("Weights must be greater than zero.")

    weighted_sum = sum(x * w for x, w in zip(numbers, weights))
    total_weight = sum(weights)

    return weighted_sum / total_weight
