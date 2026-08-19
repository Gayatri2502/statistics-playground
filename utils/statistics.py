import numpy as np
import pandas as pd
from scipy import stats


def descriptive_statistics(data):
    """
    Returns all important descriptive statistics.
    """

    values = np.array(data)

    mode_result = stats.mode(values, keepdims=True)

    return {
        "Count": len(values),
        "Mean": np.mean(values),
        "Median": np.median(values),
        "Mode": mode_result.mode[0],
        "Mode Frequency": mode_result.count[0],
        "Minimum": np.min(values),
        "Maximum": np.max(values),
        "Range": np.max(values) - np.min(values),
        "Variance": np.var(values),
        "Standard Deviation": np.std(values),
        "Q1": np.percentile(values,25),
        "Q3": np.percentile(values,75),
        "IQR": stats.iqr(values)
    }