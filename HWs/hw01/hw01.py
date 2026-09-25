"""Homework 1: Functions."""


from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = a-b
    else:
        f = a+b
    return f(a, b)


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    num=sorted([i,j,k])
    n=sorted[0]
    m=sorted[1]
    return m*m + n*n

###REVIEW
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factors are 1, 13
    1
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return n // i
    return 1

###REVIEW
def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    while True:
        if n==1:
            print(n)
            return n
        elif n % 2==0:
            n=n//2
            print(n)
        else:
            n=(n*3)+1
            print(n)

        

