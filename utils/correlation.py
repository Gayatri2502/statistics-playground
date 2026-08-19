import numpy as np


class CorrelationEngine:

    def __init__(self, df):

        self.df = df

    def covariance(self):

        return np.cov(
            self.df["Advertisement"],
            self.df["Sales"]
        )[0][1]

    def correlation(self):

        return np.corrcoef(
            self.df["Advertisement"],
            self.df["Sales"]
        )[0][1]

    def strength(self):

        corr = self.correlation()

        if corr > .9:
            return "Very Strong Positive"

        elif corr > .7:
            return "Strong Positive"

        elif corr > .4:
            return "Moderate Positive"

        elif corr > 0:
            return "Weak Positive"

        elif corr == 0:
            return "No Correlation"

        elif corr > -.4:
            return "Weak Negative"

        elif corr > -.7:
            return "Moderate Negative"

        elif corr > -.9:
            return "Strong Negative"

        return "Very Strong Negative"