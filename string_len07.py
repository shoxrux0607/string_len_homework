def main(s1, s2, s3):
    """
    Given three strings, s1, s2 and s3. 
    return their odd lengths, example "[s1, s2]".
     If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """

    satr = ""
   
    len_1 = len(s1)
    len_2 = len(s2)
    len_3 = len(s3)

    if len_1 % 2 != 0:
        if len(satr) == 0:
            satr += s1

    if len_2 % 2 != 0:
        if len(satr) == 0:
            satr += s2
        else:
            satr += ", " + s2

    if len_3 % 2 != 0:
        if len(satr) == 0:
            satr += s3
        else:
            satr += ", " + s3

    return f"[{satr}]"


print(main("codeschool.uz", "example", "python"))
