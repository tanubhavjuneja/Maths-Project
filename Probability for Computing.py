import random
import numpy as np
from scipy.stats import chisquare
def generate_uniform_numbers(seed, num_numbers):
    random.seed(seed)
    numbers = [random.uniform(0, 1) for _ in range(num_numbers)]
    return numbers
def generate_normal_numbers(seed, num_numbers, mean, std_dev):
    random.seed(seed)
    numbers = [random.normalvariate(mean, std_dev) for _ in range(num_numbers)]
    return numbers
def describe_seed_effect(dist_name, seed):
    if dist_name == generate_uniform_numbers:
        series = dist_name(seed, num_numbers)
        seed_effect = "The {} distribution is affected by the seed. Changing the seed will result in a different series of numbers, but the distribution properties (mean and standard deviation) will remain the same.".format(dist_name.__name__)
    elif dist_name == generate_normal_numbers:
        series = dist_name(seed, num_numbers, mean=0, std_dev=1)
        seed_effect = "The {} distribution is affected by the seed. Changing the seed will result in a different series of numbers, and the distribution properties (mean and standard deviation) may also change.".format(dist_name.__name__)
    return series, seed_effect
def test_randomness(series):
    observed, _ = np.histogram(series, bins='auto')
    expected = np.full_like(observed, len(series) / len(observed))
    observed_sum = observed.sum().astype(float)
    expected_sum = expected.sum().astype(float)
    observed = observed.astype(float)
    observed *= expected_sum / observed_sum
    _, p_value = chisquare(observed, f_exp=expected)
    return p_value
seed1 = 123
seed2 = 456
num_numbers = 1000
uniform_numbers = generate_uniform_numbers(seed1, num_numbers)
normal_numbers = generate_normal_numbers(seed2, num_numbers, mean=0, std_dev=1)
uniform_cycle_length = len(set(uniform_numbers))
normal_cycle_length = len(set(normal_numbers))
uniform_series, uniform_effect = describe_seed_effect(generate_uniform_numbers, seed1)
normal_series, normal_effect = describe_seed_effect(generate_normal_numbers, seed2)
uniform_p_value = test_randomness(uniform_series)
normal_p_value = test_randomness(normal_series)
print("Uniform Numbers:", uniform_numbers)
print("Normal Numbers:", normal_numbers)
print("Uniform Cycle Length:", uniform_cycle_length)
print("Normal Cycle Length:", normal_cycle_length)
print("Uniform Effect of Seed:", uniform_effect)
print("Normal Effect of Seed:", normal_effect)
print("Uniform Chi-squared p-value:", uniform_p_value)
print("Normal Chi-squared p-value:", normal_p_value)