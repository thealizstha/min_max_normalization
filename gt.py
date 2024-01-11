def min_max_normalize(data, feature_range=(0, 1)):
    """
    Perform min-max normalization on the given data.

    Parameters:
    - data: List or NumPy array of numerical values to be normalized.
    - feature_range: Tuple specifying the desired range for the normalized values (default is (0, 1)).

    Returns:
    - List of normalized values.
    """
    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        # Avoid division by zero if all values are the same
        return [feature_range[0]] * len(data)

    normalized_data = [(x - min_val) / (max_val - min_val) * (feature_range[1] - feature_range[0]) + feature_range[0] for x in data]

    return normalized_data

# Example usage:
data_to_normalize = [2, 5, 10, 15, 20]
normalized_data = min_max_normalize(data_to_normalize)

print("Original data:", data_to_normalize)
print("Normalized data:", normalized_data)
