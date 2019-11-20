from typing import Tuple
import math

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Returns mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#import os
#os.chdir("C:\\Users\\brown\\Desktop\\learning_projects\\data-science-from-scratch")
from probability import normal_cdf

# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

# It's above the threshould if it's not below the threshold
def normal_probability_above(lo: float,
                            mu: float = 0,
                            sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is greater than lo"""
    return 1 - normal_cdf(lo, mu, sigma)

# It's between if it's less than hi but not less than lo
def normal_probability_between(lo: float,
                                hi: float,
                                mu: float = 0,
                                sigma: float = 1) -> float:
    """The probability than an N(mu, sigma) is between lo and hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# It's outside if it's not between
def normal_probability_outside(lo: float,
                                hi: float,
                                mu: float = 0,
                                sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is not between lo and hi."""
    return 1 - normal_probability_between(lo, hi, mu, sigma)

from probability import inverse_normal_cdf

def normal_upper_bound(probability: float,
                        mu: float = 0,
                        sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability: float,
                        mu: float = 0,
                        sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symetric (about the mean) bounds that contain the specified
    probability
    """
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000,.5)

lower_bound, upper_bound = normal_two_sided_bounds(.95, mu_0, sigma_0)

# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the null hypothesis,
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

hi = normal_upper_bound(.95, mu_0, sigma_0)
# is 526 (< 531, since we need more proability in the upper tail)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability

# %% codecell
# p-values
