import sys
from enum import IntEnum

from math_fucntion import my_abs, my_sqrt
from colors import Colors

precision = 0


class InputException(Exception):
    """ Custom exception class. """

    def __init__(self, equation):
        Exception.__init__(self)
        self.equation = equation


class Degree(IntEnum):
    Zero = 0
    First = 1
    Second = 2


def get_degree(a, b, c):
    """ Returns equation degree.

    Parameters:
        a (int or float): Parameter before x^2.
        b (int or float): Parameter before x^1.
        c (int or float): Parameter before x^0.

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
        a (int or float): Parameter before x^2.
        b (int or float): Parameter before x^1.
        c (int or float): Parameter before x^0.

    Returns:
        int or float: discriminant.
    """
    return b * b - 4 * a * c


def easy_solution(c):
    if c == 0:
        print("|R (all the real numbers are solution)")
    else:
        print("The equation has no solution")
    return


def linear_equation_solution(b, c):
    print("The solution is: ".format(round(- c / b), precision))
    return


def second_degree_equation_solution(a, b, c):
    D = discriminant(a, b, c)
    if D != 0:
        sqrt = my_sqrt(my_abs(D))
        first_part = -b / (2 * a)
        second_part = sqrt / (2 * a)
        if D > 0:
            print("Discriminant greater than zero")
            print("First solution is: {0}"
                  .format(round(first_part + second_part, precision)))
            print("Second solution is: {0}"
                  .format(round(first_part - second_part, precision)))
        else:
            print("Discriminant less than zero")
            print("We have complex solution.")
            print("First solution is: {0} + {1} * i"
                  .format(round(first_part, precision), round(second_part, precision)))
            print("Second solution is: {0} - {1} * i"
                  .format(round(first_part, precision), round(second_part, precision)))
    else:
        print("Discriminant is zero")
        print("We have one double-solution.")
        print("Solution is: {0}"
              .format(round(-b / (2 * a), precision)))

    return


def reduced_form(a, b, c):
    print("Reduced form: {0} * X^2 + {1} * X^1 + {2} * X^0 = 0\n"
          .format(a, b, c))


def print_info_about_equation(a, b, c, power):
    print("\nPolynomial degree: {}\n".format(power))
    reduced_form(a, b, c)


def get_coefficients(part):
    a = 0.0
    b = 0.0
    c = 0.0

    for elem in part:
        if elem == '0' or elem == '':
            continue

        coeff, var = elem.split('*')
        var, power = var.split('^')

        if var != 'X' and var != 'x':
            raise InputException('The variable can only be X or x')

        try:
            if int(power) == Degree.Second:
                a += float(coeff)
            elif int(power) == Degree.First:
                b += float(coeff)
            elif int(power) == Degree.Zero:
                c += float(coeff)
            else:
                print("Polynomial degree: {0}".format(int(power)))
                sys.exit("The polynomial degree is strictly greater than 2, I can't solve.")

        except ValueError:
            raise InputException('Incorrect power. Must be greater then 0')

    return a, b, c


def solve(equation):
    a = 0
    b = 0
    c = 0

    equation = equation.replace(' ', '').replace('-', '+-').split('=')

    parts = [equation[i].split('+') for i in range(len(equation))]

    if len(parts) != 2:
        raise InputException("Wrong input. An equation has more than one equal sign or none at all")

    for index, part in enumerate(parts):
        a_tmp, b_tmp, c_tmp = get_coefficients(part)

        if index == 0:
            a += a_tmp
            b += b_tmp
            c += c_tmp
        else:
            a -= a_tmp
            b -= b_tmp
            c -= c_tmp

    degree = get_degree(a, b, c)

    print_info_about_equation(a, b, c, degree)

    if degree == Degree.Second:
        second_degree_equation_solution(a, b, c)
    elif degree == Degree.First:
        linear_equation_solution(b, c)
    else:
        easy_solution(c)

    return a, b, c


if __name__ == "__main__":
    print("Equation format: A*X^2+B*X^1+C*X^0=D*X^0.\nQuadratic polynomials or simpler.")
    equation = input("Input equation: ")

    try:
        precision = int(input("Input precision (default is 2): "))
    except ValueError:
        precision = 2

    try:
        solve(equation)
    except InputException as ex:
        print(f"{Colors.FAIL}\nInputException: Equation -- entered incorrectly.\nProblem: {ex.equation};\n"
              "Expected, for example: A*X^2+B*X^1+C*X^0=D*X^0")
