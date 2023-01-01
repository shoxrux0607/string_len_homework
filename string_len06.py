def main(s1, s2):
    """
    Given two strings, s1 and s2. 
    Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    a = len(s1)
    b = len(s2)
    if a < b:
        return s1
    else:
        return s2


print(main('code', 'exam'))
