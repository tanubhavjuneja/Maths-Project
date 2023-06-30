from math import comb, log
from scipy.stats import chisquare
class RandomGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2 ** 31
    def generate_uniform(self, n):
        series = []
        x = self.seed
        for _ in range(n):
            x = (self.a * x + self.c) % self.m
            series.append(x / self.m)
        return series
    def generate_binomial(self, n, p):
        uniform_numbers = self.generate_uniform(n)
        binomial_numbers = []
        for u in uniform_numbers:
            num_success = sum(u > sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(i + 1)) for i in range(n))
            binomial_numbers.append(num_success)
        return binomial_numbers
    def generate_exponential(self, n, rate):
        uniform_numbers = self.generate_uniform(n)
        exponential_numbers = []
        for u in uniform_numbers:
            num = -log(1 - u) / rate
            exponential_numbers.append(num)
        return exponential_numbers
    def calculate_cycle_length(self, series):
        seen = {}
        for i, num in enumerate(series):
            if num in seen:
                return i - seen[num]
            seen[num] = i
        return None
    def test_randomness(self, series):
        observed_freq = [series.count(x) for x in set(series)]
        expected_freq = [len(series) / len(set(series))] * len(set(series))
        chi2, p_value = chisquare(observed_freq, expected_freq)
        return chi2, p_value
seeds = []
seed_no = int(input("Enter the number of seeds you want to enter: "))
for i in range(seed_no):
    x = int(input("Enter Seed: "))
    seeds.append(x)
n_trials = int(input("Enter the number of trials: "))
p_success = float(input("Enter the probability of success for the binomial distribution (between 0 and 1): "))
rate = float(input("Enter the rate parameter for the exponential distribution: "))
for seed in seeds:  
    rg = RandomGenerator(seed)
    binomial_numbers = rg.generate_binomial(n_trials, p_success)
    exponential_numbers = rg.generate_exponential(n_trials, rate)
    binomial_cycle_length = rg.calculate_cycle_length(binomial_numbers)
    exponential_cycle_length = rg.calculate_cycle_length(exponential_numbers)
    binomial_chi2, binomial_p_value = rg.test_randomness(binomial_numbers)
    exponential_chi2, exponential_p_value = rg.test_randomness(exponential_numbers)
    print("Binomial Random Numbers:", binomial_numbers)
    print("Binomial Cycle Length:", binomial_cycle_length)
    print("Binomial Chi-squared Test: chi2 =", binomial_chi2, "p-value =", binomial_p_value)
    print("Exponential Random Numbers:", exponential_numbers)
    print("Exponential Cycle Length:", exponential_cycle_length)
    print("Exponential Chi-squared Test: chi2 =", exponential_chi2, "p-value =", exponential_p_value)
