from math import *


def main(s):
    """
    Given variable type string s. 
    Return the character in the middle.
    If the length is even, 
    return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """

    lens = len(s)
    if lens % 2 == 0:
        harf = s[floor(lens/2-1):floor(lens/2+1)]

    else:
        harf = s[floor(lens/2)]
    return harf


print(main("askotpsd"))
