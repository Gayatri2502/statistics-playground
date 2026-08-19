import numpy as np


class SamplingEngine:

    def __init__(self, population):

        self.population = np.array(population)

    def random_sample(self, sample_size):

        return np.random.choice(
            self.population,
            sample_size,
            replace=False
        )

    def sample_mean(self, sample):

        return np.mean(sample)

    def population_mean(self):

        return np.mean(self.population)

    def simulate_clt(
            self,
            sample_size,
            simulations=500
    ):

        means = []

        for _ in range(simulations):

            sample = np.random.choice(
                self.population,
                sample_size,
                replace=True
            )

            means.append(
                np.mean(sample)
            )

        return np.array(means)