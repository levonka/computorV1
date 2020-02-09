def my_abs(x):
    """ Returns the absolute value of number.

    Parameters:
        x (int or float): The number which is to be absolute.

    Returns:
        int or float: The number which became absolute.
    """
    return x if x > 0 else -x


def my_sqrt(n, EPS=1E-10):
    """ Returns the sqrt value of number.
        The Newton method.

    Parameters:
        n (int or float): The positive number from which the square root will be extracted.
        EPS (float): The required accuracy of calculations.

    Returns:
        float: Square root of a number.
    """
    x = 1
    while 1:
        nx = (x + n / x) / 2
        if abs(x - nx) < EPS:
            break
        x = nx
    return x
