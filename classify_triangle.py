"""
Testing Triangle Classification
@uthor : Adithya Varma Created on: 02/03/20
"""
# pylint: disable=C0103

def classify_triangle(a, b, c):
    """ Function that determines the type of triangle """
    if  isinstance(a, str)  or isinstance(b, str) or isinstance(c, str):
        return 'It is an Invalid Triangle'
    elif a + b <= c or b + c <= a or c + a <= b:
        return 'It is an Invalid Triangle'
    else:
        if a == b == c:
            return 'It is an Equilateral Triangle'
        elif a == b or b == c or a == c:
            return 'It is an Isoceles Triangle'
        elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
            return 'It is a Right Triangle'
        else:
            return 'It is a Scalene Triangle'
def main():
    """ Function that gets the input from the user """
    print('Enter the sides of the triangle')
    x_a = int(input('a = '))
    y_b = int(input('b = '))
    z_c = int(input('c = '))
    print(classify_triangle(x_a, y_b, z_c))

main()
