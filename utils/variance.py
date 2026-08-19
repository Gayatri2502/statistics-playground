import numpy as np

def calculate_statistics(values):
    values = np.array(values)

    return {
        "Mean": np.mean(values),
        "Variance": np.var(values),
        "Std Dev": np.std(values),
        "Min": np.min(values),
        "Max": np.max(values),
        "Range": np.max(values)-np.min(values)
    }