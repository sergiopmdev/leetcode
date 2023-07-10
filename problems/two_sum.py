from typing import List, Union


def two_sum(nums: List[int], target: int) -> Union[List[int], None]:
    """
    Extract the pair of numbers if any that
    when added together equal the target value

    Parameters
    ----------
    nums : List[int]
        Array of numbers from which to extract the pair
    target : int
        Number to be added by the pair of numbers

    Returns
    -------
    Union[List[int], None]
        Either the combination of two numbers
        that add up to the target or None
        in case it does not exist
    """

    for index_a in range(0, len(nums)):
        for index_b in range(index_a + 1, len(nums)):
            if nums[index_a] + nums[index_b] == target:
                return [index_a, index_b]


# LeetCode link: https://leetcode.com/problems/two-sum/
