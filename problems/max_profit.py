from typing import List


def max_profit(self, prices: List[int]) -> int:
    """
    Find the buy and sell values in a
    linearly way that return the most profit

    Parameters
    ----------
    prices : List[int]
        List of numbers in which to find those that
        linearly return maximum buy and sell returns

    Returns
    -------
    int
        Maximum profit
    """

    buy = prices[0]
    maximum_profit = 0

    for index in range(1, len(prices)):
        price = prices[index]
        if buy > price:
            buy = price
        elif price - buy > maximum_profit:
            maximum_profit = prices[index] - buy

    return maximum_profit


# LeetCode link: https://leetcode.com/problems/two-sum/
