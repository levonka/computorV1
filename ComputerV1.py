import sys
from enum import Enum

class InputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, equation):
        Exception.__init__(self)
        self.equation = equation

class Degree(Enum):
    Zero = 0
    First = 1
    Second = 2

def my_abs(x):
    """ Returns the absolute value of number.

    Parameters:
        x (int or float): The number which is to be absolute.

    Returns:
        int or float: The number which became absolute.
    """
    return x if x > 0 else -x

def my_sqrt(n, EPS = 1E-10):
    """ Returns the sqrt value of number. 
        The Newton method.

    Parameters:
        n (int or float): The positive number from which the square root will be extracted.
        EPS (float): The required accuracy of calculations.

    Returns:
        float: Square root of a number.
    """
    x = 1
    while (1):
        nx = (x + n / x) / 2
        if abs(x - nx) < EPS:
            break
        x = nx
    return x

def degree(a, b, c):
    """ Returns equation degree. 

    Parameters:
        a (int or float): Parametr before x^2.
        b (int or float): Parametr before x^1.
        c (int or float): Parametr before x^0.

    Returns:
        int: equation degree.
    """
    if a == 0 and b == 0:
        return Degree.Zero
    elif a == 0:
        return Degree.First
    else:
        return Degree.Second

def discriminant(a, b, c):
    """ Returns the discriminant.

    Parameters:
        a (int or float): Parametr before x^2.
        b (int or float): Parametr before x^1.
        c (int or float): Parametr before x^0.

    Returns:
        int or float: discriminant.
    """
    return b * b - 4 * a * c

def easy_solv(c):
    if c == 0:
        print("|R")
    else:
        print("The equation has no solution")
    return

def linear_equation_solv(b, c):
    print("The solution is: " -c / b)
    return

def second_degree_equation_solv(a, b, c):
    D = discriminant(a, b, c)
    if D != 0:
        sqrt = my_sqrt(my_abs(D))
        first_solv = (-b + sqrt) / (2 * a)
        second_solv = (-b - sqrt) / (2 * a)
        if D > 0:
            print("Discriminant greater than zero")
            print("First solution is: ", format(first_solv, '.2f'))
            print("Second solution is: ", format(second_solv, '.2f'))
        else:
            print("Discriminant less than zero")
            print("We have complex solution.")
            print("First solution is: ", format(first_solv, '.2f'))
            print("Second solution is: ", format(second_solv, '.2f'))
    else:
        print("Discriminant is zero")
        print("We have one double-solution.")
        print("Solution is: ", format(-b / (2 * a), '.2f'))

    return

def test(x):
    if x != 'X':
        raise InputException(x)
    return

if __name__== "__main__":
    try:
        print(test('lol'))
    except InputException as ex:
        print('InputException: Уравнение -- {0} введено не корректно;\nОжидалось, например: a*X^2+b*X^1+c*X^0=0'.format(ex.equation))
    #print(my_abs.__doc__ )