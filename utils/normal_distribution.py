import numpy as np
from scipy.stats import norm


class NormalDistribution:

    def __init__(self, data):
        self.data = np.array(data)

        self.mean = np.mean(self.data)
        self.std = np.std(self.data)

    def pdf(self, x):

        return norm.pdf(
            x,
            self.mean,
            self.std
        )

    def cdf(self, x):

        return norm.cdf(
            x,
            self.mean,
            self.std
        )

    def probability_between(
            self,
            lower,
            upper
    ):

        return (
            self.cdf(upper)
            -
            self.cdf(lower)
        )

    def probability_less(self, x):

        return self.cdf(x)

    def probability_greater(self, x):

        return 1-self.cdf(x)