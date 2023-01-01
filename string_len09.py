def main(num1, num2):
    """
    Given two non-negative integers,
     num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    number1 = int(num1)
    number2 = int(num2)
    number3 = number1 + number2

    return str(number3)


print(main('12', '51'))
