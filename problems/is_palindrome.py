def is_palindrome(self, num: int) -> bool:
    """
    Check if a number is a palindrome

    Parameters
    ----------
    num : int
        Number to be checked

    Returns
    -------
    bool
        True if the number is a
        palindrome or False if it is not
    """

    str_x = str(num)
    return str_x == str_x[::-1]


# LeetCode link: https://leetcode.com/problems/palindrome-number/
