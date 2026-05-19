"""contains helper functions for the rest of the code"""

def normalize(strategy: list) -> list:
    """
    Normalize a list of nonnegative numbers so they sum to 1.
    If all values are zero, return a uniform distribution.
    """
    total = sum(strategy)
    if total > 0:
        return [v/total for v in strategy]
    n = len(strategy)
    if n == 0:
        return []
    return [1.0 / n for _ in range(n)]
    

def regret_matching(regret_sum: list):
    """
    Converts cumulative regrets into a strategy.

    Positive regrets get probability proportional to their size.
    Negative regrets are treated as zero.
    """
    return normalize([max(0.0, v) for v in regret_sum])

def get_average_strategy(strategy_sum):
    """cummulative strat made into an average"""
    return normalize(strategy_sum)
